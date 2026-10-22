from fastapi import FastAPI, HTTPException
import requests
from schemas.pokemon import Pokemon
from clients.pokeapi import get_pokemon_from_api, get_pokemon_fr_name, get_fr_type_name, get_pre_evolution
from db.database import get_connection
from repositories.pokemon_repository import insert_pokemon, get_pokemon_by_number, get_all_pokemons
from services.pokemon_service import scan_pokemon

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue sur le Pokedex"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/pokemons/{number}")
def get_pokemon_from_db(number: int):
    data = get_pokemon_by_number(number)
    if (data == 0):
        raise HTTPException(status_code=404, detail="Pokemon non présent dans la base de données")
    else :
        return data 



@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon_route(number: int):
    return scan_pokemon(number)

@app.get("/pokemons")
def get_all_pokemons_from_db():
    return get_all_pokemons()

@app.get("/test/{number}")
def test(number):
    try:
        data = get_pokemon_by_number(number)
    except requests.RequestException:
        raise HTTPException(status_code=404, detail="Impossible de récupérer le Pokémon")
    return data

