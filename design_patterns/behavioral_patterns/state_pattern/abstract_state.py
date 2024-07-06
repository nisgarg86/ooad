"""
abstract state class for vending machine
"""

from abc import ABC, abstractmethod

class AbstractState(ABC):

    def set_context(self, context):
        self.context = context

    @abstractmethod
    def insert_money(self):
        raise NotImplementedError

    @abstractmethod
    def select_product(self):
        raise NotImplementedError

    @abstractmethod
    def confirm_product(self):
        raise NotImplementedError

    @abstractmethod
    def dispense_item(self):
        raise NotImplementedError

    @abstractmethod
    def return_change(self):
        raise NotImplementedError
