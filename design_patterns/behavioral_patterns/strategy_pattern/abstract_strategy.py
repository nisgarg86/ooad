"""
abstract strategy class for strategy pattern
"""

from abc import ABC, abstractmethod


class AbstractStrategy(ABC):

    @abstractmethod
    def calculate_bet_price(self):
        raise NotImplementedError

    @abstractmethod
    def place_roulette_bet(self):
        raise NotImplementedError