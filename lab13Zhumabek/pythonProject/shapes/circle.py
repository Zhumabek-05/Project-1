# shapes/circle.py
from math import pi
from shapes.base import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
