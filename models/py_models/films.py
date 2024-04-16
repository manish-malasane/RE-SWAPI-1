"""
Pydantic model for characters which are coming from swapi.dev
Notes -
Error:-
pydantic.error_wrappers.ValidationError
"""

from models.datamodel import DataModel
from typing import List, Optional


class Films(DataModel):
    director: str
    episode_id: int
    opening_crawl: str
    producer: str
    release_date: str
    title: str

    characters: Optional[List[str]]
    vehicles: Optional[List[str]]
    starships: Optional[List[str]]
    species: Optional[List[str]]
    planets: Optional[List[str]]


if __name__ == "__main__":
    data = {
        "characters": [
            "https://swapi.dev/api/people/1/",
        ],
        "created": "2014-12-10T14:23:31.880000Z",
        "director": "George Lucas",
        "edited": "2014-12-12T11:24:39.858000Z",
        "episode_id": 4,
        "opening_crawl": """It is a period of civil war.Rebel spaceships, striking from a hidden base, have won their 
        first victory against  the evil Galactic Empire.During the battle, Rebel  spies managed to steal secret plans to
        the Empire's  ultimate weapon,the DEATH  STAR, an armored space  station with enough power to destroy an entire
        planet.Pursued by the Empire's  sinister agents, Princess  Leia races home aboard her  starship, custodian of 
        the  stolen plans that can save her  people and restore  freedom to the galaxy....""",
        "planets": [
            "https://swapi.dev/api/planets/1/",
        ],
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25",
        "species": [
            "https://swapi.dev/api/species/1/",
        ],
        "starships": [
            "https://swapi.dev/api/starships/2/",
        ],
        "title": "A New Hope",
        "url": "https://swapi.dev/api/films/1/",
        "vehicles": [
            "https://swapi.dev/api/vehicles/4/",
        ],
    }

    result = Films(**data)
    print(result)
