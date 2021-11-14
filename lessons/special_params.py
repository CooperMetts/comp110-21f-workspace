"""Examples of optional parameters and Union type parameters."""

# importing the 'Union' type allows you to make a parameter either one type or another — ex: def hello(name: Union[str, int])
from typing import Union

# the = "World" part of the hello parameter is an optional value, meaning that if you don't provide an argument for the parameter, it will use "World" for name
# if you wrote something like: x: int — it would be a required parameter. 
# required parameters must come FIRST, optional parameters must come after the required ones. Ex: def hello(x: int, name: str = "World") where x is a required parameter bc you're not giving it a default value and name is an optional parameter because you are giving it a default value of "World"
# Note: once you start giving arguments/valyes to optional parameters, you have to specify ALL the optional parameters leading up to the ones you gave the value/argument to
def hello(name: Union[str, int]) -> str: 
    """A delightful greeting function."""
    result: str = "Hello, "
    # this isinstance function allows you to tell Python what to do if the 'either-or' parameter is whatever type, in this example, it's a type str
    if isinstance(name, str): 
        return result + name
    elif isinstance(name, float): 
        return result + "alien from sector " + str(name)
    else: 
        return result + "COMP 110" + str(name)

# Calling hello with no arguments leads to use of default value, if you have one in there. See above comments for examples of default values. 
print(hello())

# Calling hello with one argument overrides the default value
print(hello("John"))