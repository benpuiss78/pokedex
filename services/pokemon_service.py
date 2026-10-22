import requests
from fastapi import HTTPException
from clients.pokeapi import get_pokemon_from_api, get_pre_evolution, get_pokemon_fr_name, get_fr_type_name
from repositories.pokemon_repository import get_pokemon_by_number, insert_pokemon, get_fr_type_by_name, insert_type
from schemas.pokemon import Pokemon

def get_french_type_name(type_name : str):
    fr_type = get_fr_type_by_name(type_name)
    if(fr_type != 0):
        return fr_type.name_fr
    else:
        fr_type = get_fr_type_name(type_name)
        insert_type(fr_type)
        return fr_type.name_fr
    

def scan_pokemon(number : int):
    if get_pokemon_by_number(number) == 0: #si 0, le pokemon n'esr pas présent dans la base, on l'ajoute donc
        try:
            pokemon_data = get_pokemon_from_api(number)
            fr_name = get_pokemon_fr_name(number)
            fr_types = [get_french_type_name(t["type"]["name"]) for t in pokemon_data["types"]]
            pre_evolution_number = get_pre_evolution(number)
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
            evolves_from_number=pre_evolution_number,
        )
        insert_pokemon(pokemon)
        return pokemon
    else: #Si le pokemon est deja dans la database, on renvoie simplement ses infos
        pokemon = get_pokemon_by_number(number)
        return pokemon

