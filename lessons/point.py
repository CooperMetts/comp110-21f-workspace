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
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)

# this holds the 'scaled_point' return after calling the scale method (scale(2.0))
p1: Point = p0.scale(2.0)
print(f"{p1.x}, {p1.y}")
