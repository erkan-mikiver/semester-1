# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

import math

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

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
        area = (self.radius**2)*(math.pi)
        return round(area, 2)
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

p = Point(2, 5)
c = Circle(p, 10)

print(c.area())

print(c.perimeter())
   

