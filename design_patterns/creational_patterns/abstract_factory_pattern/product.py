
from product import Engine, Seat, Wheel, Tyre


class SportsEngine(Engine):
    def start(self):
        print("Sports Engine started")

    def stop(self):
        print("Sports Engine stopped")


class SportsSeat(Seat):
    def adjust(self):
        print("Sports Seat adjusted")

    def heat(self):
        print("Sports Seat heated")


class SportsWheel(Wheel):
    def rotate(self):
        print("Sports Wheel rotated")


class SportsTyre(Tyre):
    def inflate(self):
        print("Sports Tyre inflated")

#############################

class LuxuryEngine(Engine):
    def start(self):
        print("Luxury Engine started")

    def stop(self):
        print("Luxury Engine stopped")

class LuxurySeat(Seat):
    def adjust(self):
        print("Luxury Seat adjusted")

    def heat(self):
        print("Luxury Seat heated")


class LuxuryWheel(Wheel):
    def rotate(self):
        print("Luxury Wheel rotated")


class LuxuryTyre(Tyre):
    def inflate(self):
        print("Luxury Tyre inflated")

#############################

class SUVEngine(Engine):
    def start(self):
        print("SUV Engine started")

    def stop(self):
        print("SUV Engine stopped")


class SUVSeat(Seat):
    def adjust(self):
        print("SUV Seat adjusted")

    def heat(self):
        print("SUV Seat heated")


class SUVWheel(Wheel):
    def rotate(self):
        print("SUV Wheel rotated")


class SUVTyre(Tyre):
    def inflate(self):
        print("SUV Tyre inflated")
