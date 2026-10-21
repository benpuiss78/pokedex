from fastapi import FastAPI, HTTPException
import requests
from schemas.pokemon import Pokemon
from clients.pokeapi import get_pokemon_from_api
from db.database import get_connection
from repositories.pokemon_repository import insert_pokemon

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue sur le Pokedex"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/pokemons/{number}")
def get_pokemon(number: int):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(number)

    reponse = requests.get(url)
    err_code = reponse.status_code

    if err_code != 200:
        raise HTTPException(status_code=err_code, detail = "Erreur")
    
    data = reponse.json()
    return {
        "number": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    data = get_pokemon_from_api(number)
    if isinstance(data, int):
        raise HTTPException(status_code=data, detail = "Erreur")
    pokemon = Pokemon(
        number=data["id"],
        name=data["name"],
        name_fr=data["name"],
        types=[t["type"]["name"] for t in data["types"]],
        image_url=data["sprites"]["front_default"],
        height=data["height"],
        weight=data["weight"],
        evolves_from_number=0,
    )
    insert_pokemon(pokemon)
    return pokemon