"""
The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we would like you to use a random
number generator that picks a number between 1-82. Using these random numbers you will be pulling 15 characters from the
 API using Python.
"""

import argparse
from utility import timing, random_num_gen
from utility.urls_ import get_url, fetch_data


@timing.deco
def final_call():
    # here you can provide info related to the project
    parser = argparse.ArgumentParser(
        prog="SwapiAPI",
        usage="Fetch the data from swapi.dev based on whatever input we provide",
        description="fetches the data of random chars based on resource id's",
    )

    # this attribute help us to create an options just like `ls` linux command
    parser.add_argument(
        "-s", "--start", help="start of fetching the data of resource id's", default=1
    )
    parser.add_argument("-e", "--end", help="where to stop", default=83)
    parser.add_argument(
        "-c", "--count", help="fetches the data of n number of resource id's", default=5
    )
    parser.add_argument(
        "-r",
        "--resource",
        help="fetches the data of provided resource",
        default="people",
        choices=["people", "films", "starships", "vehicle", "species", "planets"],
    )

    # helps us to parse the options which we create using the `parser.add_argument()`
    arguments = parser.parse_args()

    ip = random_num_gen.IteratorProtocol(
        int(arguments.start), int(arguments.end), int(arguments.count)
    )
    result = [number for number in ip]
    # print(result)
    actor_names = []
    for resource_id in result:
        url = get_url(arguments.resource, resource_id)
        di_data = fetch_data(url)
        # capturing the names from dict object
        actor_names.append(di_data.get("name"))

    print(actor_names)
    """-----------------------------------------------"""


if __name__ == "__main__":
    final_call()
