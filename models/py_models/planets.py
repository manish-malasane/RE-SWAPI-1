"""
Pydantic model for characters which are coming from swapi.dev
Notes -
Error:-
pydantic.error_wrappers.ValidationError
"""

from models.datamodel import DataModel
from typing import List, Optional


class Planets(DataModel):
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

    films: List[Optional[str]]
    residents: List[Optional[str]]


if __name__ == "__main__":
    data = {
        "climate": "Arid",
        "created": "2014-12-09T13:50:49.641000Z",
        "diameter": "10465",
        "edited": "2014-12-15T13:48:16.167217Z",
        "films": [
            "https://swapi.dev/api/films/1/",
        ],
        "gravity": "1",
        "name": "Tatooine",
        "orbital_period": "304",
        "population": "120000",
        "residents": [
            "https://swapi.dev/api/people/1/",
        ],
        "rotation_period": "23",
        "surface_water": "1",
        "terrain": "Dessert",
        "url": "https://swapi.dev/api/planets/1/",
    }
    result = Planets(**data)
    print(result)
