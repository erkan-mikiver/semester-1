# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# Tomato
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# Union of two sets and both sets contain tomato
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add('strawberry')
# Remove an item from vegetables
vegetables.discard('leek')
# Find and display symmetric difference of the two sets
symmetric_diff = fruit.symmetric_difference(vegetables)
print(symmetric_diff)