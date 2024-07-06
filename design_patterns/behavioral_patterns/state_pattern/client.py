"""
client code for vending machine
"""


from context import VendingMachine
from state import ProductSelection


def main():

    vending_machine = VendingMachine()
    vending_machine.set_state(ProductSelection())
    vending_machine.select_product()
    vending_machine.confirm_product()
    vending_machine.insert_money()
    vending_machine.select_product()
    vending_machine.confirm_product()
    vending_machine.insert_money()
    vending_machine.dispense_item()
    vending_machine.return_change()


if __name__ == '__main__':
    main()