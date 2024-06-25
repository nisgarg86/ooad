"""
director class for the builder pattern
"""

from builder import BurgerBuilder


class BurgerDirector:

    def __init__(self, builder: BurgerBuilder):
        self.builder = builder
    
    def make_simple_burger(self, bread_type: str, patty_type: str):
        self.builder.add_bread(bread_type)
        self.builder.add_patty(patty_type)
    
    def make_veg_burger(self, bread_type: str, patty_type: str, veggies_type: str):
        self.builder.add_bread(bread_type)
        self.builder.add_veggies(patty_type)
        self.builder.add_patty(veggies_type)
    
    def make_cheese_burger(self, bread_type: str, patty_type: str, cheese_type: str):
        self.builder.add_bread(bread_type)
        self.builder.add_cheese(patty_type)
        self.builder.add_patty(cheese_type)
    
    def make_non_veg_burger(self, bread_type: str, patty_type: str, meat_type: str):
        self.builder.add_bread(bread_type)
        self.builder.add_meat(meat_type)
        self.builder.add_patty(patty_type)
    
    def make_saucy_burger(self,
                          bread_type: str,
                          patty_type: str, 
                          sauce_type: str, 
                          veggies_type: str, 
                          cheese_type: str):
        self.builder.add_bread(bread_type)
        self.builder.add_cheese(cheese_type)
        self.builder.add_veggies(veggies_type)
        self.builder.add_sauce(sauce_type)
        self.builder.add_patty(patty_type)
    
    def reset_builder(self, builder: BurgerBuilder):
        self.builder = builder

