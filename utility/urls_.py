import json
import typing
import requests
from utility.logger_file import mylogger


def get_url(resource: str, id_: int) -> str:
    """This function will generate the url based on inputs"""

    home_url = "https://swapi.dev"
    relative_url = f"/api/{resource}/{id_}/"
    abs_url = home_url + relative_url
    return abs_url


def fetch_data(url: str) -> typing.Dict:
    """Function took the generated random url from get_url() & fetches the data from a swapi.dev and returns a python
    dictionary data"""

    response = requests.get(url)  # returns an HTTP's response object
    # if we get status code == 200 then and only then perform next operations
    if response.status_code != 200:
        response.raise_for_status()
    else:
        data = json.loads(response.text)
        return data

    # if response.status_code == 200:
    #     data = response.text  # will get `stringified` version of data
    #     dic_data = json.loads(data)  # it will convert json data into a python dict data [serialization]
    #     return dic_data
