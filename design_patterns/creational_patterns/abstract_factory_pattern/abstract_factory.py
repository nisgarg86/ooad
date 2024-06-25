
from abc import ABC, abstractmethod

from abstract_product import Engine, Seat, Wheel, Tyre


class CarFactory(ABC):

    def __init__(self) -> None:
        self.engine = self.create_engine()
        self.seat = self.create_seat()
        self.wheel = self.create_wheel()
        self.tyre = self.create_tyre()

    @abstractmethod
    def create_engine(self) -> Engine:
        raise NotImplementedError

    @abstractmethod
    def create_seat(self) -> Seat:
        raise NotImplementedError
    
    @abstractmethod
    def create_wheel(self) -> Wheel:
        raise NotImplementedError
    
    @abstractmethod
    def create_tyre(self) -> Tyre:
        raise NotImplementedError

    def start_car(self):
        self.engine.start()
        self.seat.adjust()
        self.seat.heat()
        self.tyre.inflate()
        self.wheel.rotate()
    
    def stop_car(self):
        self.engine.stop()
