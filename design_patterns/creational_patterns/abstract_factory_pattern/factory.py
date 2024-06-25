
from product import SportsEngine, SportsSeat, SportsWheel, SportsTyre, LuxuryEngine, LuxurySeat, LuxuryWheel, LuxuryTyre, SUVEngine, SUVSeat, SUVWheel, SUVTyre
from abstract_factory import CarFactory
from abstract_product import Engine, Seat, Wheel, Tyre

class SportsCarFactory(CarFactory):

    def __init__(self) -> None:
        super().__init__()

    def create_engine(self) -> Engine:
        return SportsEngine()

    def create_seat(self) -> Seat:
        return SportsSeat()

    def create_wheel(self) -> Wheel:
        return SportsWheel()

    def create_tyre(self) -> Tyre:
        return SportsTyre()


class LuxuryCarFactory(CarFactory):
    
        def __init__(self) -> None:
            super().__init__()
    
        def create_engine(self) -> Engine:
            return LuxuryEngine()
    
        def create_seat(self) -> Seat:
            return LuxurySeat()
    
        def create_wheel(self) -> Wheel:
            return LuxuryWheel()
    
        def create_tyre(self) -> Tyre:
            return LuxuryTyre()


class SUVFactory(CarFactory):

    def __init__(self) -> None:
        super().__init__()

    def create_engine(self) -> Engine:
        return SUVEngine()

    def create_seat(self) -> Seat:
        return SUVSeat()

    def create_wheel(self) -> Wheel:
        return SUVWheel()

    def create_tyre(self) -> Tyre:
        return SUVTyre()
