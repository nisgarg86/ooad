"""
concrete state classes for vending machine
"""

import random

from abstract_state import AbstractState


class ProductSelection(AbstractState):
    """
    idle state class
    """

    def __init__(self) -> None:
        self.context = None

    def insert_money(self):
        print("please select a product first...!")
        return

    def select_product(self):
        product = input("Enter product name: ")
        self.context.set_product(product)
        self.context.set_product_price(100 + random.randint(0, 100))
        print(f"product selected - {product}...!")

    def confirm_product(self):
        print(f'Product confirmed - {self.context.get_product()}...!')
        print('Please input Money now...!')
        self.context.set_state(MoneyInput())
    
    def dispense_item(self):
        print('Please select a product first...!')
        return
    
    def return_change(self):
        print('Please select a product first...!')
        return


class MoneyInput(AbstractState):

    def __init__(self) -> None:
        self.context = None

    def insert_money(self):
        money = int(input("Enter amount: "))
        self.context.set_money(money)
        print(f"Money inserted - {money}...!")
        self.context.set_state(DispenseItem())

    def select_product(self):
        print(f'Accepting money - {self.context.get_money()}...!')

    def confirm_product(self):
        print(f'Product already selected - {self.context.get_product()}...!')
    
    def dispense_item(self):
        print('Please insert money first...!')
        return
    
    def return_change(self):
        print('Please insert money first...!')
        return


class DispenseItem(AbstractState):

    def __init__(self) -> None:
        self.context = None

    def insert_money(self):
        print("Money already inserted...!")
        return

    def select_product(self):
        print(f'Product already selected - {self.context.get_product()}...!')

    def confirm_product(self):
        print(f'Product already selected - {self.context.get_product()}...!')
    
    def dispense_item(self):
        product = self.context.get_product()
        money = self.context.get_money()
        product_price = self.context.get_product_price()
        if money >= product_price:
            print(f'Item dispensed - {product}...!')
            change = money - product_price
        else:
            print('Insufficient money...!')
            change = money
        self.context.set_return_change(change)
        self.context.set_state(ReturnChange())
    
    def return_change(self):
        print('Currently dispensing item...!')
        return


class ReturnChange(AbstractState):

    def __init__(self) -> None:
        self.context = None

    def insert_money(self):
        print("Item already dispensed...!")
        return

    def select_product(self):
        print(f'Item already dispensed - {self.context.get_product()}...!')

    def confirm_product(self):
        print(f'Item already dispensed - {self.context.get_product()}...!')
    
    def dispense_item(self):
        print(f'Item already dispensed - {self.context.get_product()}...!')
        return
    
    def return_change(self):
        change = self.context.get_return_change()
        print(f'Returning change - {change}...!')
        self.context.set_state(ProductSelection())
