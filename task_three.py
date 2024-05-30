"""
Import all the resource classes
get count of each resource
get singular resource url from each resource
pull data from random 3 singular resource urls
convert task three into cli
"""
import argparse
from pprint import pprint
from utility.random_num_gen import IteratorProtocol
from utility.timing import deco
from utility.urls_ import fetch_data
from Resources.films import Film
from Resources.peoples import People
from Resources.starships import Starship
from Resources.species import Specie
from Resources.vehicles import Vehicle
from Resources.planets import Planet

from models.py_models.films import Films
from models.py_models.planets import Planets
from models.py_models.species import Species
from models.py_models.vehicles import Vehicles
from models.py_models.starships import Starships
from models.py_models.people import Peoples

films_urls = []
planet_urls = []
specie_urls = []
vehicle_urls = []
starship_urls = []
people_urls = []


def film_data_():
    Film().get_count()
    # ("Films:- ", Film().get_count())

    film_data = Film().get_random_data(1)
    # print("Film_data", Films(**film_data))
    Films(**film_data)

    global films_urls
    films_urls = Film().get_resource_urls()


def people_data_():
    People().get_count()
    # print("Peoples:- ", People().get_count())

    people_data = People().get_random_data(1)
    Peoples(**people_data)
    # print("People_data", Peoples(**people_data))

    global people_urls
    people_urls = People().get_resource_urls()


def starship_data_():
    Starship().get_count()
    # print("Starships:- ", Starship().get_count())

    starship_data = Starship().get_random_data(2)
    Starships(**starship_data)
    # print("Starship_data", Starships(**starship_data))

    global starship_urls
    starship_urls = Starship().get_resource_urls()


def specie_data_():
    Specie().get_count()
    # print("Species:- ", Specie().get_count())

    specie_data = Specie().get_random_data(1)
    Species(**specie_data)
    # print("Specie_data", Species(**specie_data))

    global specie_urls
    specie_urls = Specie().get_resource_urls()


def vehicle_data_():
    Vehicle().get_count()
    # print("Vehicles:- ", Vehicle().get_count())

    vehicle_data = Vehicle().get_random_data(4)
    Vehicles(**vehicle_data)
    # print("Vehicle_data", Vehicles(**vehicle_data))

    global vehicle_urls
    vehicle_urls = Vehicle().get_resource_urls()


def planet_data_():
    Planet().get_count()
    # print("Planets:- ", Planet().get_count())

    planet_data = Planet().get_random_data(1)
    Planets(**planet_data)
    # print("Planet_data", Planets(**planet_data))

    global planet_urls
    planet_urls = Planet().get_resource_urls()


def main():
    film_data_()
    specie_data_()
    starship_data_()
    planet_data_()
    people_data_()
    vehicle_data_()


@deco
def random_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", default=1, type=int)
    parser.add_argument("-e", "--end", default=6, type=int)
    parser.add_argument("-l", "--limit", default=3, type=int)
    parser.add_argument("-r", "--resource", default="people", choices=["people",
                                                                       "vehicles",
                                                                       "planets",
                                                                       "species",
                                                                       "starships",
                                                                       "films"])

    arguments = parser.parse_args()
    result = IteratorProtocol(arguments.start, arguments.end, arguments.limit)
    resources = [element for element in result]
    breakpoint()
    for item in resources:
        if arguments.resource == "films":
            data = fetch_data(films_urls[item])
            pprint(data)
        elif arguments.resource == "people":
            data = fetch_data(people_urls[item])
            pprint(data)
        elif arguments.resource == "planets":
            data = fetch_data(planet_urls[item])
            pprint(data)
        elif arguments.resource == "species":
            data = fetch_data(specie_urls[item])
            pprint(data)
        elif arguments.resource == "starships":
            data = fetch_data(starship_urls[item])
            pprint(data)
        else:
            data = fetch_data(vehicle_urls[item])
            pprint(data)


if __name__ == "__main__":
    main()
    random_data()
