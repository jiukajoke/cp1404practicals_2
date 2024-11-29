class Taxi:
    def __init__(self, name, fuel, price_per_km):
        self.name = name
        self.fuel = fuel
        self.price_per_km = price_per_km
        self.total_distance = 0
        self.total_fare = 0

    def drive(self, distance):
        if distance <= self.fuel:
            self.fuel -= distance
            self.total_distance += distance
            self.total_fare += distance * self.price_per_km
        else:
            print(f"Not enough fuel to drive {distance} km!")

    def restart_meter(self):
        self.total_distance = 0
        self.total_fare = 0

    def get_details(self):
        return f"Taxi Name: {self.name}\nFuel: {self.fuel} units\nPrice per km: ${self.price_per_km:.2f}\n"

    def get_current_fare(self):
        return f"Current Fare: ${self.total_fare:.2f}\n"
