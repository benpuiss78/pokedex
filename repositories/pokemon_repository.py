import json
from schemas.pokemon import Pokemon
from schemas.type import Type
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

def get_fr_type_by_name(type_name: str):
    connection = get_connection()
    cursor = connection.execute(
        "SELECT * FROM pokemon_types WHERE name = ?", (type_name,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return 0
    return Type(
        id=row["id"],
        name=row["name"],
        name_fr=row["name_fr"],
    )

def insert_type(type : Type):
        connection = get_connection()
        connection.execute(
                """
                INSERT INTO pokemon_types
                (
                    id,
                    name,
                    name_fr
                )
                VALUES (?, ?, ?)
                """,
                (
                    type.id,
                    type.name,
                    type.name_fr,
                )
            )
        connection.commit()
        connection.close()

def get_all_pokemons():
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM pokemon ORDER BY number")
    rows = cursor.fetchall()
    connection.close()
    result = []
    for row in rows:
        pokemon = Pokemon(
            number=row["number"],
            name=row["name"],
            name_fr=row["name_fr"],
            types=json.loads(row["types"]),
            image_url=row["image_url"],
            height=row["height"],
            weight=row["weight"],
            evolves_from_number=row["evolves_from_number"],
        )
        result.append(pokemon)
    return result
    