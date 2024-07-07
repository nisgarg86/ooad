"""
client code for strategy pattern
"""


from player import Player
from strategy import MartingaleStrategy, FibonacciStrategy, LabouchereStrategy


def main():
    player = Player("John")
    
    print('changing strategy to Martingale...!')

    martingale = MartingaleStrategy()
    player.set_strategy(martingale)
    player.calculate_bet_price()
    player.place_roulette_bet()

    print('changing strategy to Fibonacci...!')
    
    fibonacci = FibonacciStrategy()
    player.set_strategy(fibonacci)
    player.calculate_bet_price()
    player.place_roulette_bet()

    print('changing strategy to Labouchere...!')
    
    labouchere = LabouchereStrategy()
    player.set_strategy(labouchere)
    player.calculate_bet_price()
    player.place_roulette_bet()

if __name__ == "__main__":
    main()
