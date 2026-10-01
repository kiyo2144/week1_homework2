import random

numbers = [1, 2, 3, 4, 5, 6]


def dice():
    return random.choice(numbers)


print(dice())
