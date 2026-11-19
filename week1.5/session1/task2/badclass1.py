# A bad class implementation

# What does the runtime error mean?

## Point(1.5, 2.0) creates an object and automatically passes the instance to __init__, but the constructor 
# only declares two parameters, causing the error

# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
