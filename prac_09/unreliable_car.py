import random

class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def drive(self, distance):
        if self.fuel >= distance:
            self.fuel -= distance
            return distance
        else:
            driven_distance = self.fuel
            self.fuel = 0
            return driven_distance

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
