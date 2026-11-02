# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if type(width) is not int or type(height) is not int:
            raise TypeError
        elif width <= 0 or height <= 0:
            raise ValueError
        
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns a boolean value whether the shape is a square or not.
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Calculates the Area of the Shape from the given height and width values.
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        Calculates the Perimeter of the Shape from the given height and width values.
        """
        perimeter = (2*self.width) + (2*self.height)
        return perimeter


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
