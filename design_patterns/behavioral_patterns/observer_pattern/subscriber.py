"""
concrete subscriber class
"""

from abstract_subscriber import AbstractSubscriber


class StockSubscriber(AbstractSubscriber):

    def __init__(self, name):
        self.name = name

    def update(self, *args, **kwargs):
        print(f'{self.name} received update for stock price for {args[1]}: {args[0]}')
    
    def __repr__(self) -> str:
        return f'({self.name})'