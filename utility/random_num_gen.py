"""Module belongs to generate the n number of random numbers between the provided range using random module"""
from random import randint


class IteratorProtocol(object):
    """
    Iterator Protocol which generates 15 random numbers within the given range
    """

    def __init__(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.limit:
            self.start += 1
            return randint(self.start, self.end)
        else:
            raise StopIteration
