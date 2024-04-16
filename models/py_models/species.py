"""
Pydantic model for characters which are coming from swapi.dev
Notes -
Error:-
pydantic.error_wrappers.ValidationError
"""

from models.datamodel import DataModel
from typing import List, Optional


class Species(DataModel):
    average_height: str
    average_lifespan: str
    classification: str
    designation: str
    eye_colors: str
    hair_colors: str
    homeworld: str
    language: str
    name: str
    skin_colors: str

    people: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":
    data = {
        "average_height": "2.1",
        "average_lifespan": "400",
        "classification": "Mammal",
        "created": "2014-12-10T16:44:31.486000Z",
        "designation": "Sentient",
        "edited": "2014-12-10T16:44:31.486000Z",
        "eye_colors": "blue, green, yellow, brown, golden, red",
        "hair_colors": "black, brown",
        "homeworld": "https://swapi.dev/api/planets/14/",
        "language": "Shyriiwook",
        "name": "Wookie",
        "people": ["https://swapi.dev/api/people/13/"],
        "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/"],
        "skin_colors": "gray",
        "url": "https://swapi.dev/api/species/3/",
    }
    result = Species(**data)
    print(result)
