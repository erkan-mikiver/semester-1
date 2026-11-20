# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import *

point = Point(0.5, 0.5)
circle = Circle(2.5)


if point in circle:
    print("point is inside circle!")


