
from factory import SportsCarFactory, LuxuryCarFactory, SUVFactory


def main():

    sports_car_factory = SportsCarFactory()
    sports_car_factory.start_car()
    sports_car_factory.stop_car()

    print('-----------')

    luxury_car_factory = LuxuryCarFactory()
    luxury_car_factory.start_car()
    luxury_car_factory.stop_car()

    print('-----------')

    suv_factory = SUVFactory()
    suv_factory.start_car()
    suv_factory.stop_car()


if __name__ == "__main__":
    main()