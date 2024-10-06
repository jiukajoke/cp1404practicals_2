is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop when a valid integer is entered
    except ValueError:  # Catch the ValueError exception, which is raised when the input cannot be converted to an integer
        print("Please enter a valid integer.")
print("Valid result is:", result)
