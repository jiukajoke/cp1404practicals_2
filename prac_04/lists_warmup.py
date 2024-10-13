numbers = [3, 1, 4, 1, 5, 9, 2]

# Accessing elements
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

# Modifying the list
numbers[0] = "ten"
numbers[-1] = 1

# Printing elements except the first two
print(numbers[2:])

# Checking if 9 is an element of numbers
print(9 in numbers)
