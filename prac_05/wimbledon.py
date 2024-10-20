import csv

def read_wimbledon_data(filename):
    champions = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row

        for row in reader:
            champion_name = row[2]
            champion_country = row[1]

            # Process the champions and countries
            if champion_name in champions:
                champions[champion_name] += 1
            else:
                champions[champion_name] = 1
            countries.add(champion_country)

    return champions, countries

def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)

    # Display the champions and their win counts
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    # Display the countries of the champions in alphabetical order
    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries_string)

if __name__ == "__main__":
    main()
