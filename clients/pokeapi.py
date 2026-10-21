import requests

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

def get_fr_type_name(type):
    url = "https://pokeapi.co/api/v2/type/" + type
    reponse = requests.get(url)
    reponse.raise_for_status()
    data = reponse.json()
    for x in data["names"]:
        if x["language"]["name"] == "fr":
            return x["name"]
    return data["name"]

def get_pre_evolution(number):
    url = "https://pokeapi.co/api/v2/pokemon-species/"+  str(number)
    reponse = requests.get(url)
    reponse.raise_for_status()
    return reponse.json()