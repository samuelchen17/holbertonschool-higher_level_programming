"""Module that defines CountedIterator Class"""


class CountedIterator:
    """CountedIterator class"""

    def __init__(self, iterable):
        """initialize iterator and counter"""
        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item
