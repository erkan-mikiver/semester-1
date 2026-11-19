# Week 1.5, Session 1: Task 3

import math

class Point:
    """
    A Point in 2D space.
    """
    
    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, x2, y2):
        """
        Returns the distance from the point and another distinct point
        """
        return math.dist((self.x, self.y), (x2, y2))



# Finally, add code here to demonstrate use of Point

p = Point(1.5, 3.0)

print(p.distance())

print(p.distance_to(5, 6))
