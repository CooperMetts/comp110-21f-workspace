"""Example of a class and object instantiation."""

# instantiation definition: 


# names of classes start with capital letters 
class Pizza: 
    """Models the idea of a pizza."""

    # Attribute Definitions
    size: str = "Small"
    toppings: int = 0
    extra_cheese: bool = False

    # 'pizza' --> the name of the parameter — 'Pizza' --> the type that the parameter 'pizza' accepts

    def __init__(self, size: str, toppings: int): 
        """Constructor definition for intialization of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float: 
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total = total + 10.0
        else: 
            total = total + 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total = total + 1.0

        total = total * tax

        return total


# this is a varible of type Pizza and it will consrtruction a new Pizza object
# 'Pizza()' is a constructer call, which is a type of function call
a_pizza: Pizza = Pizza("large", 3)  # <-- using init (initalize) in the Pizza object elemenates the need for the lines below because those variables are intialized in the Pizza object
# a_pizza.size = "large"
# a_pizza.toppings = 3
# a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}.")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price ${another_pizza.price(1.05)}.")
