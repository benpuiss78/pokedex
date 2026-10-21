from fastapi import FastAPI, HTTPException
import requests
from schemas.pokemon import Pokemon
from clients.pokeapi import get_pokemon_from_api, get_pokemon_fr_name
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
        raise HTTPException(status_code=err_code, detail = "Erreur " +str(data))
    
    data = reponse.json()
    return {
        "number": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    pokemon_data = get_pokemon_from_api(number)
    fr_name = get_pokemon_fr_name(number)
    if isinstance(pokemon_data, int):
        raise HTTPException(status_code=pokemon_data, detail = "Erreur " +str(pokemon_data))
    if isinstance(fr_name, int):
            raise HTTPException(status_code=fr_name, detail = "Erreur " +str(fr_name))
    pokemon = Pokemon(
        number=pokemon_data["id"],
        name=pokemon_data["name"],
        name_fr=str(fr_name),
        types=[t["type"]["name"] for t in pokemon_data["types"]],
        image_url=pokemon_data["sprites"]["front_default"],
        height=pokemon_data["height"],
        weight=pokemon_data["weight"],
        evolves_from_number=0,
    )
    #insert_pokemon(pokemon)
    return pokemon

