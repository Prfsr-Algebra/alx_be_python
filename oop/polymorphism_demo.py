# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method for calculating area, meant to be overridden"""
        raise NotImplementedError("The area method must be overridden by a subclass")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor for Rectangle class"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Constructor for Circle class"""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * (self.radius ** 2)

