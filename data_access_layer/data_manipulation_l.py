from data_access_layer.db_connection import get_toml_conn
import pydantic
from typing import List
from pymysql import IntegrityError


def insert_entry(tb_name: str, pk: str, pk_val: int, cols: List, vals: List):
    col_names = ", ".join(cols)
    try:
        val_fields = ", ".join(vals)
    except (pydantic.ValidationError, TypeError) as ex:
        print(f"[ ERROR ] None values are not allowed instead specify str - {ex}")

    val_fields = ""

    for val in vals:
        if isinstance(val, str):
            val_fields = val_fields + '''"''' + val + '''"''' + ""","""
        elif isinstance(val, int):
            val_fields = val_fields + str(val) + """, """
        else:
            val_fields = val_fields + "Null" + ""","""

    val_fields = val_fields.rstrip(",")
    result = None

    with get_toml_conn() as connection:
        conn = connection.cursor()
        sql_query = f"insert into starwarsdb.{tb_name} ({pk}, {col_names})" \
                    f"values ({pk_val}, {val_fields})"

        try:
            result = conn.execute(sql_query)
            connection.commit()
        except IntegrityError as entry:
            print(f"[ ERROR ] entry is already stored in the database - {entry}")

    return result


if __name__ == "__main__":
    insert_entry(
        "species",
        "species_id",
        1,
        [
            "name",
            "classification",
            "designation",
            "average_height",
            "skin_colors",
            "hair_colors",
            "eye_colors",
            "average_lifespan",
            "homeworld",
            "language",
        ],
        [
            "Human",
            "mammal",
            "sentient",
            "180",
            "caucasian, black, asian, hispanic",
            "blonde, brown, black, red",
            "brown, blue, green, hazel, grey, amber",
            "120",
            "https://swapi.dev/api/planets/9/",
            "Galactic Basic",
        ],
    )
