"""Example of a Point class."""
from __future__ import annotations
# the above thing imports something so that we can return point in the scale method


class Point:    
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x,y components."""
        self.x *= x
        self.y *= y

    # this one DOES mutate the Point object — see method-call_mutation for help
    def scale_by(self, factor: float) -> None:
        """Mutates: multipliees components by factor."""
        self.x *= factor
        self.y *= factor


    # since this one returns scaled_point, it's not mutating the values of the Point object
    def scale(self, factor: float) -> Point:
        """Pure method (method as in method call or constructor call) that does not mutate the Point."""
        # to write this scale method using operator overloading: 
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point

    # IMPORTANT Note: define either of __repr__ or __str__ (interchangeable in COMP 110, not in real life) on the class of that object to make it be able to understand how to convert 0's and 1's to an actual str. 
    # Makes lines of code below from having to do: p1: Point = p0.scale(2.0) & print(f"{p1.x}, {p1.y}") to only having to write: p1_as_a_str: str = str(p1) & print(p1_as_a_str)
    # essentially enables you to be able to print actual strs using your class

    # essentially this makes your str not look like a bunch of 0's and 1's. Try commenting and uncommenting this section of code out then running python -m lessons.point to see the difference it makes.  
    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    # if you don't define a __str__ method, the __repr__ method gets called by default
    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for point * float --> essentially explain how to multiply a float by a point to Python."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point: 
        # rhs means right hand side
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1: 
            return self.y
        elif:
            raise IndexError


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)

# this holds the 'scaled_point' return after calling the scale method (scale(2.0))
p1: Point = p0.scale(2.0)
print(f"{p1.x}, {p1.y}")
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1) 
print(p1_repr)
