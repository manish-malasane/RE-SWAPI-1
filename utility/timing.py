"""Module belongs to get an execution time of a function in seconds"""
from time import time


def deco(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"[ INFO ] Time taken for an execution is:- {end - start}")
        return result

    return wrapper
