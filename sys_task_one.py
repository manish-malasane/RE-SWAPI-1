"""
The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we would like you to use a random
number generator that picks a number between 1-82. Using these random numbers you will be pulling 15 characters from the
 API using Python.
"""

from sys import argv
from utility import timing, random_num_gen
from utility.urls_ import get_url, fetch_data


@timing.deco
def final_call():
    rand = random_num_gen.IteratorProtocol(int(argv[1]), int(argv[2]), int(argv[3]))
    result = [number for number in rand]
    # print(result)

    actor_names = []
    for resource_id in result:
        url = get_url(argv[4], resource_id)
        di_data = fetch_data(url)
        actor_names.append(di_data.get("name"))

    print(actor_names)
    """---------------------------------------------------------------------------------------------------------"""


if __name__ == "__main__":
    final_call()
