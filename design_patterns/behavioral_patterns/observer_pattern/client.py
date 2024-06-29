"""
client class for the observer pattern
"""


from stock_updater import StockUpdater
from subscriber import StockSubscriber


def main():

    stock_updater = StockUpdater()

    subscriber1 = StockSubscriber('sub1')
    subscriber2 = StockSubscriber('sub2')
    subscriber3 = StockSubscriber('sub3')

    stock_updater.stock_notifier.add_subscriber('AAPL', subscriber1)
    stock_updater.stock_notifier.add_subscriber('AAPL', subscriber2)
    stock_updater.stock_notifier.add_subscriber('GOOGL', subscriber3)
    stock_updater.stock_notifier.add_subscriber('GOOGL', subscriber2)
    stock_updater.stock_notifier.add_subscriber('MSFT', subscriber3)

    stock_updater.update_stock_price('AAPL', 100.0)
    stock_updater.update_stock_price('GOOGL', 200.0)
    stock_updater.update_stock_price('AAPL', 150.0)
    stock_updater.update_stock_price('MSFT', 300.0)


if __name__ == '__main__':
    main()
