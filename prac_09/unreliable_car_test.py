from unreliable_car import UnreliableCar

# Create an UnreliableCar
my_unreliable_car = UnreliableCar("UnreliableCar 1", 100, 70)  # Name, fuel, reliability

# Attempt to drive the car 50 km (reliability is 70%)
distance_driven = my_unreliable_car.drive(50)

# Print the result
if distance_driven > 0:
    print(f"{my_unreliable_car.name} drove {distance_driven} km.")
else:
    print(f"{my_unreliable_car.name} failed to start.")

# Attempt to drive the car 30 km (reliability is 70%)
distance_driven = my_unreliable_car.drive(30)

# Print the result
if distance_driven > 0:
    print(f"{my_unreliable_car.name} drove {distance_driven} km.")
else:
    print(f"{my_unreliable_car.name} failed to start.")
