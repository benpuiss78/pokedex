import requests
from schemas.type import Type

def get_pokemon_from_api(number):
    url = "https://pokeapi.co/api/v2/pokemon/"+  str(number)
    reponse = requests.get(url)
    reponse.raise_for_status()
    return reponse.json()

def get_pokemon_fr_name(number):
    url = "https://pokeapi.co/api/v2/pokemon-species/"+  str(number)
    reponse = requests.get(url)
    reponse.raise_for_status()
    data = reponse.json()
    for x in data["names"]:
        if x["language"]["name"] == "fr":
            return x["name"]
    return data["name"]    #Si pas de nom francais, on renvoie le nom original en anglais

def get_fr_type_name(type_name: str):
    url = "https://pokeapi.co/api/v2/type/" + type_name
    reponse = requests.get(url, timeout=10)
    reponse.raise_for_status()
    data = reponse.json()

    name_fr = type_name  # secours : nom anglais
    for x in data["names"]:
        if x["language"]["name"] == "fr":
            name_fr = x["name"]
            break
    return Type(id=data["id"], name=type_name, name_fr=name_fr)

def get_pre_evolution(number):
    url = "https://pokeapi.co/api/v2/pokemon-species/"+  str(number)
    reponse = requests.get(url)
    reponse.raise_for_status()
    data = reponse.json()
    if data["evolves_from_species"] is None:
        return 0
    url_pre_evolution = data["evolves_from_species"]["url"]
    morceaux_url = url_pre_evolution.split("/")
    pre_evolution_number = int(morceaux_url[6]) #Le 7eme élément de l'url correspon au number du pokemon
    if pre_evolution_number > 151:
        return 0
    return pre_evolution_number