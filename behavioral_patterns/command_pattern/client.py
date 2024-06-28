"""
client code for command pattern
"""


from command_pattern.concrete_command import PlaceOrderCommand, CancelOrderCommand
from command_pattern.invoker import OrderApp
from command_pattern.receiver import OrderSystem

if __name__ == '__main__':

    order_system = OrderSystem()

    place_order_command = PlaceOrderCommand(order_system, 'bob', 'item1', 2)
    cancel_order_command = CancelOrderCommand(order_system, 'order1')

    order_app = OrderApp(place_order_command, cancel_order_command)

    order_app.place_order()
    order_app.cancel_order()