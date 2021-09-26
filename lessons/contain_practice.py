"""Example of a function that processes a list."""


def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i = i + 1
    return False


# Notes: 

# Define the function named contains
# We can give two arguments: a needle value wee'ree searching for in a haystack list
    # Should return true if needle is found in haystack, false otherwise 
    # Loop through eaach index in list
    # Test if item stored at index is equal to needle
    # Return true if so
# Return false after testing each item
