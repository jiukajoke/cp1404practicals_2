import random

def generate_quick_pick(min_number, max_number, numbers_per_line):
    return sorted(random.sample(range(min_number, max_number + 1), numbers_per_line))

def main():
    try:
        num_quick_picks = int(input("How many quick picks? "))
        if num_quick_picks <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    min_number = 1
    max_number = 45
    numbers_per_line = 6

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick(min_number, max_number, numbers_per_line)
        print(" ".join(f"{num:2d}" for num in quick_pick))

if __name__ == "__main__":
    main()
