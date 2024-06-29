"""
concrete iterator class for the iterator pattern
"""

from collections.abc import Iterator


class SimpleIterator(Iterator):
    """
    concrete iterator class for the iterator pattern
    """

    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration

    def has_next(self):
        """
        check if there are more items in the collection
        """
        return self._index < len(self._collection)


class AlternateIterator(Iterator):
    """
    concrete iterator class for the iterator pattern
    """

    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 2
            return item
        raise StopIteration

    def has_next(self):
        """
        check if there are more items in the collection
        """
        return self._index < len(self._collection)