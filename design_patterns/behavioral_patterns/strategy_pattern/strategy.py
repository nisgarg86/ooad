"""
concrete strategy classes for strategy pattern
"""

from abstract_strategy import AbstractStrategy


class MartingaleStrategy(AbstractStrategy):

    def __init__(self) -> None:
        self.context = None
    
    def set_context(self, context):
        self.context = context

    def calculate_bet_price(self):
        print("Martingale strategy: double the bet after every loss")
    
    def place_roulette_bet(self):
        print("Martingale strategy: place a bet on red or black")


class FibonacciStrategy(AbstractStrategy):

    def __init__(self) -> None:
        self.context = None
    
    def set_context(self, context):
        self.context = context

    def calculate_bet_price(self):
        print("Fibonnaci strategy: sum of the two preceding bets")
    
    def place_roulette_bet(self):
        print("Fibonnaci strategy: place a bet on odd or even")


class LabouchereStrategy(AbstractStrategy):

    def __init__(self) -> None:
        self.context = None
    
    def set_context(self, context):
        self.context = context

    def calculate_bet_price(self):
        print("Labouchere strategy: sum of the first and last numbers in the sequence")
    
    def place_roulette_bet(self):
        print("Labouchere strategy: place a bet on high or low")
