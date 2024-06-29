"""
stock updater class for observer pattern
"""

from publisher import StockNotifier


class StockUpdater:

    def __init__(self):
        self.stock_notifier = StockNotifier()
        self.stock_price_dict = {}

    def update_stock_price(self, stock_name: str, stock_price: float) -> None:
        self.stock_price_dict[stock_name] = stock_price
        self.stock_notifier.notify_subscribers(stock_name, stock_price)
