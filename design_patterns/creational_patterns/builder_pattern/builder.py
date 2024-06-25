"""
builder class
"""

from abc import ABC, abstractmethod

from product import McDonaldsBurger, BurgerKingBurger


class BurgerBuilder(ABC):
    """
    Abstract builder class
    """

    @abstractmethod
    def add_bread(self, bread: str):
        """
        Add bread
        """
        pass

    @abstractmethod
    def add_meat(self, meat: str):
        """
        Add meat
        """
        pass

    @abstractmethod
    def add_patty(self, patty: str):
        """
        Add patty
        """
        pass

    @abstractmethod
    def add_cheese(self, cheese: str):
        """
        Add cheese
        """
        pass

    @abstractmethod
    def add_sauce(self, sauce: str):
        """
        Add sauce
        """
        pass

    @abstractmethod
    def add_veggies(self, veggies: str):
        """
        Add veggies
        """
        pass

    @abstractmethod
    def get_burger(self):
        """
        Get burger
        """
        pass


class McDonaldsBurgerBuilder(BurgerBuilder):

    def __init__(self):
        self.burger = McDonaldsBurger()
    
    def add_bread(self, bread: str):
        self.burger.bread = bread
    
    def add_meat(self, meat: str):
        self.burger.meat = meat
    
    def add_patty(self, patty: str):
        self.burger.patty = patty
    
    def add_cheese(self, cheese: str):
        self.burger.cheese = cheese
    
    def add_sauce(self, sauce: str):
        self.burger.sauce = sauce

    def add_veggies(self, veggies: str):
        self.burger.veggies = veggies

    def get_burger(self):
        burger = self.burger
        self.burger = McDonaldsBurger()
        return burger


class BurgerKingBurgerBuilder(BurgerBuilder):

    def __init__(self):
        self.burger = BurgerKingBurger()
    
    def add_bread(self, bread: str):
        self.burger.bread = bread
    
    def add_meat(self, meat: str):
        self.burger.meat = meat
    
    def add_patty(self, patty: str):
        self.burger.patty = patty
    
    def add_cheese(self, cheese: str):
        self.burger.cheese = cheese
    
    def add_sauce(self, sauce: str):
        self.burger.sauce = sauce

    def add_veggies(self, veggies: str):
        self.burger.veggies = veggies

    def get_burger(self):
        burger = self.burger
        self.burger = BurgerKingBurger()
        return burger
