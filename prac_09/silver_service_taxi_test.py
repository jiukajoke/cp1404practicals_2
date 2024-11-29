from silver_service_taxi import SilverServiceTaxi

def main():
    taxi1 = SilverServiceTaxi("Hummer", 200, 4)
    taxi2 = SilverServiceTaxi("Limo", 100, 2)

    trip_distance = 18

    fare1 = taxi1.get_fare(trip_distance)
    fare2 = taxi2.get_fare(trip_distance)

    print(f"{taxi1}\nFare for an {trip_distance} km trip: ${fare1:.2f}")
    print(f"{taxi2}\nFare for an {trip_distance} km trip: ${fare2:.2f}")

if __name__ == "__main__":
    main()
