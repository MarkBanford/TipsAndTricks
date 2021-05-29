import random


def power_of_2(fnc):
    def inner():  # no arguments as random_odd_digit has no arguments
        return fnc() ** 2

    return inner


@power_of_2
def random_odd_digit():
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
