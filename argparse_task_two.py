"""
1) Pull data for the first movie in star wars
2) Write the json data into a file named output.txt

SUBTASKS -
1. Output should be only list of names (first name & last name) of characters in the
movie.
2. Output should only pprint list of planet names used in the movie
3. Output should only pprint list of vehicle names used in the movie.

"""

import argparse
from pprint import pprint
from utility.urls_ import get_url, fetch_data
from utility import timing


@timing.deco
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--resource",
        default="films",
        help="fetch the data of film from swapi.dev",
    )
    parser.add_argument(
        "-id",
        "--resource_id",
        default=1,
        help="fetch the data of 1st film from swapi.dev",
    )
    arguments = parser.parse_args()
    url = get_url(arguments.resource, arguments.resource_id)
    data = fetch_data(url)

    chars_urls = data.get("characters")
    planet_urls = data.get("planets")
    vehicles_urls = data.get("vehicles")

    char_names = []
    for i in chars_urls:
        char_data = fetch_data(i)
        char_names.append(char_data.get("name"))

    planet_names = []
    for i in planet_urls:
        planet_data = fetch_data(i)
        planet_names.append(planet_data.get("name"))

    vehicle_names = []
    for i in vehicles_urls:
        vehicle_data = fetch_data(i)
        vehicle_names.append(vehicle_data.get("name"))

    pprint(char_names)
    print()
    pprint(planet_names)
    print()
    pprint(vehicle_names)


if __name__ == "__main__":
    # result = main()
    # pprint(result)
    main()
