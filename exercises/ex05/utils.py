"""List utility functions part 2."""

__author__ = "730336784"

# Define your functions below


list_1: list[int] = [6, 7, 8, 9, 10]


def only_evens(a: list) -> list: 
    """Takes evens of list."""
    i: int = 0
    evens_list: list[int] = [] 
    while i < len(a): 
        if a[i] % 2 == 0:
            evens_list.append(a[i])
        i = i + 1
    return evens_list


list_2: list[int] = [1, 2, 3, 4, 5]


def sub(x: list, y: int, z: int) -> list:
    """Makes subset of list."""
    sub_set: list[int] = []
    if y == len(x) or z <= 0 or x == []:
        return []
    while y < z:
        if y >= 0 and z < len(x):
            sub_set.append(x[y])
            y = y + 1

        if y < 0: 
            y = 0
            sub_set.append(x[y])
            y = y + 1

        if z > len(x): 
            z = len(x) - 1
        sub_set.append(x[y])
        y = y + 1

    return sub_set


print(sub(list_2, 1, 5))


def concat(h: list, i: list) -> list:
    """Concatenates two lists."""
    return h + i
