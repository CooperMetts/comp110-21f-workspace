"""List utility functions."""

__author__ = "730336784"


# TODO: Implement your functions here.

# from random import randint

# y: int = int(input("Enter a number: "))
# x: list[int] = [randint(0, 9), randint(0, 9), randint(0, 9)]


def all(x: list[int], y: int) -> bool: 
    if len(x) == 0:
        return False
    i: int = 0 
    while i < len(x):
        if x[i] != y:
            return False
        i = i + 1
    return True


# print(all(x, y))

# l_one: list = []
# l_two: list = []


def is_equal(a: list, b: list) -> bool:
    i: int = 0
    if len(a) != len(b):
        return False
    else:
        while i < len(a):
            if a[i] != b[i]:
                return False
            i = i + 1
        return True


# print(is_equal(l_one, l_two))

x: list = [0, 2, 3, 1]


def max(c: list) -> int: 
    i: int = 0
    max: int = c[i]
    next_number: int = c[i + 1] 
    while i < len(c):
        if max < next_number:
            max = next_number
        i = i + 1
    return max


print(max(x))
