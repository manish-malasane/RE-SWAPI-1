# pull the data for the first movie and save it in db
from pprint import pprint
from Resources.films import Film
from utility.urls_ import fetch_data
from data_access_layer.data_manipulation_l import insert_entry
from utility.timing import deco

from models.py_models.films import Films
from models.py_models.people import Peoples
from models.py_models.species import Species
from models.py_models.planets import Planets
from models.py_models.vehicles import Vehicles
from models.py_models.starships import Starships

from data_access_layer import db_connection


def store_char():
    characters = film_data.characters
    char_cols = [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
        "created",
        "edited",
        "url",
    ]

    for char in characters:
        response_data = fetch_data(char)
        char_data = Peoples(**response_data)
        char_vals = [
            char_data.name,
            char_data.height,
            char_data.mass,
            char_data.hair_color,
            char_data.skin_color,
            char_data.eye_color,
            char_data.birth_year,
            char_data.gender,
            char_data.homeworld,
            char_data.created.strftime("%y-%m-%d"),
            char_data.edited.strftime("%y-%m-%d"),
            char_data.url,
        ]
        char_id = int(char_data.url.split("/")[-2])
        insert_entry("characters", "char_id", char_id, char_cols, char_vals)


def store_planets():
    planets = film_data.planets
    planet_cols = [
        "name",
        "rotation_period",
        "orbital_period",
        "diameter",
        "climate",
        "gravity",
        "terrain",
        "surface_water",
        "population",
        "created",
        "edited",
        "url",
    ]
    for planet in planets:
        response_data = fetch_data(planet)
        planet_data = Planets(**response_data)
        planet_vals = [
            planet_data.name,
            planet_data.rotation_period,
            planet_data.orbital_period,
            planet_data.diameter,
            planet_data.climate,
            planet_data.gravity,
            planet_data.terrain,
            planet_data.surface_water,
            planet_data.population,
            planet_data.created.strftime("%y-%m-%d"),
            planet_data.edited.strftime("%y-%m-%d"),
            planet_data.url,
        ]

        planet_id = int(planet_data.url.split("/")[-2])
        insert_entry("planet", "planet_id", planet_id, planet_cols, planet_vals)


def store_starship():
    starships = film_data.starships
    starship_cols = [
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "hyperdrive_rating",
        "MGLT",
        "starship_class",
        "created",
        "edited",
        "url",
    ]

    for starship in starships:
        response_data = fetch_data(starship)
        starship_data = Starships(**response_data)

        starship_vals = [
            starship_data.name,
            starship_data.model,
            starship_data.manufacturer,
            starship_data.cost_in_credits,
            starship_data.length,
            starship_data.max_atmosphering_speed,
            str(starship_data.crew),
            starship_data.passengers,
            starship_data.cargo_capacity,
            starship_data.consumables,
            starship_data.hyperdrive_rating,
            starship_data.MGLT,
            starship_data.starship_class,
            starship_data.created.strftime("%y-%m-%d"),
            starship_data.edited.strftime("%y-%m-%d"),
            starship_data.url,
        ]

        starship_id = int(starship_data.url.split("/")[-2])
        insert_entry("starship", "starship_id", starship_id, starship_cols, starship_vals)


def store_vehicle():
    vehicles = film_data.vehicles
    vehicle_cols = [
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "vehicle_class",
        "created",
        "edited",
        "url",
    ]

    for vehicle in vehicles:
        response_data = fetch_data(vehicle)
        vehicle_data = Vehicles(**response_data)
        vehicle_vals = [
            vehicle_data.name,
            vehicle_data.model,
            vehicle_data.manufacturer,
            vehicle_data.cost_in_credits,
            vehicle_data.length,
            vehicle_data.max_atmosphering_speed,
            vehicle_data.crew,
            vehicle_data.passengers,
            vehicle_data.cargo_capacity,
            vehicle_data.consumables,
            vehicle_data.vehicle_class,
            vehicle_data.created.strftime("%y-%m-%d"),
            vehicle_data.edited.strftime("%y-%m-%d"),
            vehicle_data.url,
        ]

        vehicle_id = int(vehicle_data.url.split("/")[-2])
        insert_entry("vehicle", "vehicle_id", vehicle_id, vehicle_cols, vehicle_vals)


def store_species():
    species = film_data.species
    specie_cols = [
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
        "created",
        "edited",
        "url",
    ]

    for specie in species:
        response_data = fetch_data(specie)
        specie_data = Species(**response_data)

        specie_vals = [
            specie_data.name,
            specie_data.classification,
            specie_data.designation,
            specie_data.average_height,
            specie_data.skin_colors,
            specie_data.hair_colors,
            specie_data.eye_colors,
            specie_data.average_lifespan,
            specie_data.homeworld,
            specie_data.language,
            specie_data.created.strftime("%y-%m-%d"),
            specie_data.edited.strftime("%y-%m-%d"),
            specie_data.url,
        ]

        specie_id = int(specie_data.url.split("/")[-2])
        insert_entry("species", "species_id", specie_id, specie_cols, specie_vals)


def store_film():
    film_ = film_data.url
    response_data = fetch_data(film_)
    film_data_ = Films(**response_data)

    film_cols = [
        "title",
        "episode_id",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_vals = [
        film_data.title,
        film_data.episode_id,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    film_id = int(film_data_.url.split("/")[-2])
    insert_entry("film", "film_id", film_id, film_cols, film_vals)


@deco
def final_call():
    store_char()
    store_planets()
    store_starship()
    store_vehicle()
    store_species()
    store_film()


if __name__ == "__main__":
    film_obj = Film()
    film = film_obj.get_random_data(resource_id=1)
    film_data = Films(**film)

    final_call()
