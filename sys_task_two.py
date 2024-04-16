"""
1) Pull data for the first movie in star wars
2) Write the json data into a file named output.txt

SUBTASKS -
1. Output should be only list of names (first name & last name) of characters in the
movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.

"""
import json
from sys import argv
from pprint import pprint
from utility.urls_ import get_url, fetch_data
from utility import timing


@timing.deco
def main():
    url = get_url(argv[1], int(argv[2]))
    data = fetch_data(url)

    with open("output.txt", "w") as json_data:
        json_data.write(json.dumps(data))

    characters = []
    for i in data.get("characters"):
        char_data = fetch_data(i)
        characters.append(char_data.get("name"))

    planets = []
    for i in data.get("planets"):
        planet_data = fetch_data(i)
        planets.append(planet_data.get("name"))

    vehicles = []
    for i in data.get("vehicles"):
        vehicle_data = fetch_data(i)
        vehicles.append(vehicle_data.get("name"))

    pprint(characters)
    pprint(planets)
    pprint(vehicles)


if __name__ == "__main__":
    main()
