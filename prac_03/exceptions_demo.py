"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# When will a ValueError occur?
# A ValueError will occur if the user enters a value that cannot be converted to an integer. For example, if the user enters a non-numeric input, such as "abc" or "1.5", the int() function will raise a ValueError.
#
# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if the user enters a denominator value of zero. Division by zero is mathematically undefined, so Python raises a ZeroDivisionError when attempting to divide by zero.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
