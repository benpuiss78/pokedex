import requests

def get_pokemon_from_api(number):
    url = "https://pokeapi.co/api/v2/pokemon/"+  str(number)
    reponse = requests.get(url)
    err_code = reponse.status_code
    if err_code != 200:
        return err_code
    return reponse.json()

def get_pokemon_fr_name(number):
    url = "https://pokeapi.co/api/v2/pokemon-species/"+  str(number)
    reponse = requests.get(url)
    err_code = reponse.status_code
    if err_code != 200:
        return err_code
    data = reponse.json()
    for x in data["names"]:
        if x["language"]["name"] == "fr":
            return x["name"]
    return data["name"]    #Si pas de nom francais, on renvoie le nom original en anglais

def get_fr_type_name(type):
    url = "https://pokeapi.co/api/v2/type/" + type
    reponse = requests.get(url)
    err_code = reponse.status_code
    if err_code != 200:
        return err_code
    data = reponse.json()
    for x in data["names"]:
        if x["language"]["name"] == "fr":
            return x["name"]
    return data["name"]

