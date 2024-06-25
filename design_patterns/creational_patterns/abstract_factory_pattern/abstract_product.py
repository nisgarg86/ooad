"""
products.py: Define the products that the abstract factory will create.
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError


class Seat(ABC):
    @abstractmethod
    def adjust(self):
        raise NotImplementedError

    @abstractmethod
    def heat(self):
        raise NotImplementedError


class Wheel(ABC):
    @abstractmethod
    def rotate(self):
        raise NotImplementedError


class Tyre(ABC):
    @abstractmethod
    def inflate(self):
        raise NotImplementedError
