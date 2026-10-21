import json
from schemas.pokemon import Pokemon
from db.database import get_connection

def insert_pokemon(pokemon: Pokemon):
    connection = get_connection()
    connection.execute(
        """
        INSERT INTO pokemon
        (
            number,
            name,
            name_fr,
            types,
            image_url,
            height, weight,
            evolves_from_number
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon.number,
            pokemon.name,
            pokemon.name_fr,
            json.dumps(pokemon.types),
            pokemon.image_url,
            pokemon.height,
            pokemon.weight,
            pokemon.evolves_from_number
        )
    )
    connection.commit()
    connection.close()