# pull the data for the first movie and save it in db
from pprint import pprint
from Resources.films import Film
from models.py_models.films import Films


if __name__ == "__main__":
    data = Film().get_random_data(resource_id=1)

    result = Films(**data)
    pprint(result)
