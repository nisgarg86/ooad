"""
concrete command classes for command pattern
"""

from typing import Dict
from command_pattern.abstract_command import Command
from behavioral_patterns.command_pattern.receiver import OrderSystem

class PlaceOrderCommand(Command):

    def __init__(self,
                 receiver: OrderSystem,
                 user_id: str, 
                 item_code: str, 
                 quantity: int) -> None:
        self.receiver = receiver
        self.user_id = user_id
        self.item_code = item_code
        self.quantity = quantity

    def execute(self) -> None:
        self.receiver.order_queue(self.user_id, self.item_code, self.quantity)
    

class CancelOrderCommand(Command):

    def __init__(self, receiver: OrderSystem, order_id: str) -> None:
        self.receiver = receiver
        self.order_id = order_id

    def execute(self) -> None:
        self.receiver.cancel_queue(self.order_id)
