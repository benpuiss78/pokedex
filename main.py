from fastapi import FastAPI, HTTPException
import requests
import sqlite3
from pydantic import BaseModel, EmailStr, Field

class Pokemon(BaseModel):
    number : int
    name : str
    name_fr : str
    types : list[str]
    image_url : str
    height : int
    weight : int
    evolves_from_number : int

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
        return {"Erreur de récuperation des infos du Pokemon dans l'API"}
    
    data = reponse.json()
    reponse_json = {
        "number": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }
    return reponse_json

