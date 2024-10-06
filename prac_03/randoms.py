# A random integer between 5 and 20 (both inclusive).The smallest number is 5, the largest is 20.
# A random integer from the given range (3, 5, 7, or 9). The smallest number is 3, the largest is 9.No, randrange with a step of 2 could not have produced a 4, as it only generates odd numbers within the given range.
# A random float between 2.5 (inclusive) and 5.5 (exclusive). The smallest number is 2.5, and the largest close to 5.5

import random

random_number = random.randint(1, 100)
print(random_number)

