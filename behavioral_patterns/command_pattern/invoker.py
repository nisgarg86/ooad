"""
invoker class for command pattern
"""

from behavioral_patterns.command_pattern.abstract_command import Command

class OrderApp:

    def __init__(self, place_order: Command,
                 cancel_order: Command) -> None:
        self.place_order_command = place_order
        self.cancel_order_command = cancel_order
    
    def place_order(self):
        self.place_order_command.execute()
    
    def cancel_order(self):
        self.cancel_order_command.execute()



    