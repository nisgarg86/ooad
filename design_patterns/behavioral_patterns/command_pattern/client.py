"""
client code for command pattern
"""


from concrete_command import PlaceOrderCommand, CancelOrderCommand
from invoker import OrderApp
from receiver import OrderSystem

if __name__ == '__main__':

    order_system = OrderSystem()

    place_order_command = PlaceOrderCommand(order_system, 'bob', 'item1', 2)
    cancel_order_command = CancelOrderCommand(order_system, 'order1')

    order_app = OrderApp(place_order_command, cancel_order_command)

    order_app.place_order()
    order_app.cancel_order()