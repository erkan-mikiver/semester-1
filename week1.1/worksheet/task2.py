"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
not_int = True
while not_int:
    try:
        value = int(input('\nEnter an amount you would like to save every month: -> '))
        not_int = False
    except:
        print('\nPlease enter a valid amount\n\n')

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

value = value * 12

print(f'\nTotal amount saved after 12 months: £{value:.2f}')

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

value = value + (value*0.08)
print(f'\nTotal amount saved incl. interest: £{value:.2f}')