"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

import pytest

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730336784"


def test_inversion() -> None: 
    input: dict[str, str] = {"blue": "red", "green": "yellow"}
    assert invert(input) == {"red": "blue", "yellow": "green"}


with pytest.raises(KeyError): 
    input: dict[str, str] = {"blue": "yellow", "green": "yellow"}
    invert(input) 


def test_popular_color() -> None: 
    input: dict[str, str] = {"one": "blue", "two": "green", "three": "blue"}
    assert favorite_color(input) == "blue"


def test_single_color() -> None: 
    input: dict[str, str] = {"one": "green"}
    assert favorite_color(input) == "green"


def test_a_tie() -> None:
    input: dict[str, str] = {"one": "blue", "two": "blue", "three": "green", "four": "green"}
    assert favorite_color(input) == ___
