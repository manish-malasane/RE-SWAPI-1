"""
Pydantic model for characters which are coming from swapi.dev
Notes -
Error:-
pydantic.error_wrappers.ValidationError
"""

from typing import List, Optional
from models.datamodel import DataModel


class Vehicles(DataModel):
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    vehicle_class: str

    pilots: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":
    data = {
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "cost_in_credits": "150000",
        "created": "2014-12-10T15:36:25.724000Z",
        "crew": "46",
        "edited": "2014-12-10T15:36:25.724000Z",
        "length": "36.8",
        "manufacturer": "Corellia Mining Corporation",
        "max_atmosphering_speed": "30",
        "model": "Digger Crawler",
        "name": "Sand Crawler",
        "passengers": "30",
        "pilots": [],
        "films": ["https://swapi.dev/api/films/1/"],
        "url": "https://swapi.dev/api/vehicles/4/",
        "vehicle_class": "wheeled",
    }

    result = Vehicles(**data)
    print(result)
