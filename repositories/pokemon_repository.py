import json
from schemas.pokemon import Pokemon
from db.database import get_connection

def get_pokemon_by_number(number : int):
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM pokemon WHERE number = ?", (number,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return 0
    else:
        return Pokemon(
            number=row["number"],
            name=row["name"],
            name_fr=row["name_fr"],
            types=json.loads(row["types"]),
            image_url=row["image_url"],
            height=row["height"],
            weight=row["weight"],
            evolves_from_number=row["evolves_from_number"],
        )

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