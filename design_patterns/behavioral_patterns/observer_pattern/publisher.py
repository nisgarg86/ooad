"""
publisher class for observer pattern
"""

from abstract_subscriber import AbstractSubscriber
from collections import defaultdict

class StockNotifier:

    def __init__(self) -> None:
        self.__subscriber_dict = defaultdict(list)
    
    def add_subscriber(self, stock_name: str, subscriber: AbstractSubscriber) -> None:
        self.__subscriber_dict[stock_name].append(subscriber)
        print(f'{subscriber} subscribed to {stock_name}')
    
    def remove_subscriber(self, stock_name: str, subscriber: AbstractSubscriber) -> None:
        self.__subscriber_dict[stock_name].remove(subscriber)
        print(f'{subscriber} unsubscribed from {stock_name}')
    
    def notify_subscribers(self, stock_name: str, stock_price: float) -> None:
        for subscriber in self.__subscriber_dict[stock_name]:
            subscriber.update(stock_price, stock_name)