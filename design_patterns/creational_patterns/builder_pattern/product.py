"""
product class for builder pattern
we can also create a common interface for the product classes if they have similar attributes
"""

class McDonaldsBurger:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.cheese = None
        self.veggies = None
        self.sauce = None
        self.patty = None

    def __str__(self):
        return f"McDonalds Burger\nBread: {self.bread}\nMeat: {self.meat}\nCheese: {self.cheese}\nVeggies: {self.veggies}\nSauce: {self.sauce}\nPatty: {self.patty}"


class BurgerKingBurger:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.cheese = None
        self.veggies = None
        self.sauce = None
        self.patty = None

    def __str__(self):
        return f"BurgerKing Burger\nBread: {self.bread}\nMeat: {self.meat}\nCheese: {self.cheese}\nVeggies: {self.veggies}\nSauce: {self.sauce}\nPatty: {self.patty}"

