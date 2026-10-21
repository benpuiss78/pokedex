import requests

def get_pokemon_from_api(number):
    url = "https://pokeapi.co/api/v2/pokemon/"+  str(number)
    reponse = requests.get(url)
    err_code = reponse.status_code
    if err_code != 200:
        return err_code
    return reponse.json()