import sqlite3

def get_connection():
    connexion = sqlite3.connect("pokedex.db")
    connexion.row_factory = sqlite3.Row
    return connexion