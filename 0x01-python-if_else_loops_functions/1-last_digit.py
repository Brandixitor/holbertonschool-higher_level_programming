#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastDigit(n):
    if (n < 0):
        return (number % -10)
    else:
        return (number % 10)


def verif(n=number):
    if (n > 5):
        return (" and is greater than 5")
    elif (n == 0):
        return (" and is 0")
    elif (n != 0 and n < 6):
        return (" and is less than 6 and not 0")
print("Last digit of {} is {}{}".format(number, lastDigit(number), verif()))
