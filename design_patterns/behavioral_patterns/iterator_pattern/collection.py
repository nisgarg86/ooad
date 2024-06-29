"""
collection class for iterator pattern
in python, we will not create an abstract class for the collection
will use collections.abc.Iterable instead
"""


from collections.abc import Iterable, Iterator
from concrete_iterator import SimpleIterator, AlternateIterator


class NumericCollection(Iterable):
    """
    collection class for the iterator pattern
    """

    def __init__(self):
        self._collection = []

    def add(self, item):
        """
        add an item to the collection
        """
        self._collection.append(item)
    
    def get_alternate_iterator(self) -> Iterator:
        return AlternateIterator(self._collection)
    
    def __iter__(self) -> Iterator:
        return SimpleIterator(self._collection)