"""
player class
"""

from abstract_strategy import AbstractStrategy


class Player:

    def __init__(self, name):
        self.bet_price = 100
        self.winning = 0
    
    def set_strategy(self, strategy: AbstractStrategy):
        self.strategy = strategy
        self.strategy.set_context(self)
    
    def calculate_bet_price(self):
        self.strategy.calculate_bet_price()
    
    def place_roulette_bet(self):
        self.strategy.place_roulette_bet()
    
    def set_bet_price(self, bet_price):
        self.bet_price = bet_price
    
    def get_bet_price(self):
        return self.bet_price
