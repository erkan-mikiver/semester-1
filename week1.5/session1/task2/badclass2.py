# Another bad class implementation

# What does the runtime error mean?

## __init__ constructur only makes the x and y variables locally, and doesn't assign them to the actual Point instance,
# so they are unable to be accessed outside of the constructor

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
