"""Practice with dictionaries."""

__author__ = "730336784"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """This inverts the values and keys of a given function."""
    output: dict[str, str] = {}
    for key in x:
        output[x[key]] = key
    return output


def favorite_color(x: dict[str, str]) -> str: 
    """This identifies the most popular color in a given dictionary."""
    # making a new  dictonary
    common_color: dict[str, int] = {}
    # checking for each key of the key-value pair in x (the input/given dictonary)
    for key in x:
        # this assigns the value of each key in x to the variable color, on each check or loop through the dictonary
        color: str = x[key]
        if color in common_color: 
            # this is saying if the given colors, which are from the values of the input/given dictonary, are already in the new dictonary (common_colors), then update that key (color) in common colors by + 1
            common_color[color] = common_color[color] + 1
        else:
            # this is saying if the given colors are NOT already in the new dictonary (common_colors), put there key in and set there value to 1
            common_color[color] = 1

    # this is just telling the for...in loop that color is a str
    color: str 
    # this is creating a new variable for the below for...in loop that keeps track of which color has the highest score
    max: int = 0
    # this is saying that popular color is an exmpt str. It is used when the current max (which is the color with the highest score in the dictonary at the time) is less whatever key the for...in loop is on, so then that new color with the higher  score becomes the  popular_color
    popular_color: str = ""

    for color in common_color: 
        if max < common_color[color]:
            max = common_color[color]
            popular_color = color
    return popular_color


def count(x: list[str]) -> dict[str, int]:
    """This counts the number of times an item occurs in a string."""
    built: dict[str, int] = {}
    for item in x: 
        if item in built:
            built[item] = built[item] + 1
        else:
            built[item] = 1
    return built
