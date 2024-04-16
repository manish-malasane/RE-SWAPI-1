"""
Pydantic model for characters which are coming from swapi.dev
Notes -
Error:-
pydantic.error_wrappers.ValidationError
"""

from models.datamodel import DataModel
from typing import List, Optional


class Starships(DataModel):
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    starship_class: str

    pilots: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":
    data = {
        "MGLT": "10 MGLT",
        "cargo_capacity": "1000000000000",
        "consumables": "3 years",
        "cost_in_credits": "1000000000000",
        "created": "2014-12-10T16:36:50.509000Z",
        "crew": "342953",
        "edited": "2014-12-10T16:36:50.509000Z",
        "hyperdrive_rating": "4.0",
        "length": "120000",
        "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
        "max_atmosphering_speed": "n/a",
        "model": "DS-1 Orbital Battle Station",
        "name": "Death Star",
        "passengers": "843342",
        "films": ["https://swapi.dev/api/films/1/"],
        "pilots": [],
        "starship_class": "Deep Space Mobile Battlestation",
        "url": "https://swapi.dev/api/starships/9/",
    }

    result = Starships(**data)
    print(result)
