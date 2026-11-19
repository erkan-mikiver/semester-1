# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:
    """
    A circle in 2D space
    """
    def __init__(self, point, radius):
        """
        Creates a Circle, given the centre and radius
        """
        self.centre = point
        self.radius = radius
    
    def area(self):
        """
        Calculates the area of the circle
        """
        area = (self.radius**2)*(math.pi)
        return round(area, 2)
    
    def perimeter(self):
        """
        Calculates the perimeter of the circle
        """
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)


# Don't add any testing code to this file!
