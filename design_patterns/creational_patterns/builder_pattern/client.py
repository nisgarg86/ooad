"""
client code for builder pattern
"""

from builder import McDonaldsBurgerBuilder, BurgerKingBurgerBuilder
from director import BurgerDirector


if __name__ == '__main__':

    mc_donalds_burger_builder = McDonaldsBurgerBuilder()
    burger_director = BurgerDirector(mc_donalds_burger_builder)
    burger_director.make_saucy_burger("multigrain", "chicken", "mayo", "lettuce", "cheddar")
    mc_donalds_burger = mc_donalds_burger_builder.get_burger()
    print(mc_donalds_burger)

    print('-----------------------------------')

    burger_king_burger_builder = BurgerKingBurgerBuilder()
    burger_director.reset_builder(burger_king_burger_builder)
    burger_director.make_veg_burger("wheat", "veggie", "lettuce, tomato, onion")
    burger_king_burger = burger_king_burger_builder.get_burger()
    print(burger_king_burger)