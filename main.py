from fastapi import FastAPI, HTTPException
import requests
from schemas.pokemon import Pokemon
from clients.pokeapi import get_pokemon_from_api, get_pokemon_fr_name, get_fr_type_name
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

    try:
        reponse = requests.get(url)
    except requests.RequestException:
        raise HTTPException(status_code=404, detail="Impossible de récupérer le Pokémon")
    data = reponse.json()
    return {
        "number": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    try:
        pokemon_data = get_pokemon_from_api(number)
        fr_name = get_pokemon_fr_name(number)
        fr_types = [get_fr_type_name(t["type"]["name"]) for t in pokemon_data["types"]]
    except requests.RequestException:
        raise HTTPException(status_code=404, detail="Impossible de récupérer le Pokémon")
         
    pokemon = Pokemon(
        number=pokemon_data["id"],
        name=pokemon_data["name"],
        name_fr=str(fr_name),
        types=fr_types,
        image_url=pokemon_data["sprites"]["front_default"],
        height=pokemon_data["height"] * 10, #conversion en cm
        weight=pokemon_data["weight"] * 100, # conversion en grammes
        evolves_from_number=0,
    )
    #insert_pokemon(pokemon)
    return pokemon

