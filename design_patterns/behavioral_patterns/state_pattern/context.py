"""
vending machine class that uses state pattern, it is a singleton class
"""


from abstract_state import AbstractState


class VendingMachine:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.product = None
        self.product_price = None
        self.money = None
        self.return_money = None

    def set_state(self, state: AbstractState):
        self.state = state
        self.state.set_context(self)

    def set_product(self, product):
        self.product = product

    def set_product_price(self, price):
        self.product_price = price

    def set_money(self, money):
        self.money = money
    
    def set_return_change(self, money):
        self.return_money = money

    def get_product(self):
        return self.product

    def get_product_price(self):
        return self.product_price

    def get_money(self):
        return self.money

    def get_return_change(self):
        return self.return_money

    def insert_money(self):
        self.state.insert_money()

    def select_product(self):
        self.state.select_product()

    def confirm_product(self):
        self.state.confirm_product()

    def dispense_item(self):
        self.state.dispense_item()

    def return_change(self):
        self.state.return_change()
