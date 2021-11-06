"""Tests for the sum function."""

# this imports the function sum from sum module (or file) in the lessons folder
from lessons.sum import sum


def test_sum_empty() -> None: 
    # assert that something is true based on how you expect the function to behave
    # this asserts that if you give the sum function an empty list, it will return a value of 0.0
    assert sum([]) == 0.0


def test_sum_single_item() -> None: 
    assert sum([110.0])


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0 
