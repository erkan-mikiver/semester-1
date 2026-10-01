"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""



# TODO: wrap the risky operations in a try/except block
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds

invalid = True
while invalid:
    try:
        numerator_input = input("\nEnter the numerator: ")
        numerator = int(numerator_input)

        denominator_input = input("\nEnter the denominator: ")
        denominator = int(denominator_input)

        final = numerator / denominator

        invalid = False

    except ValueError:
        print('\n\nERROR: Enter a valid numerical value')

    except ZeroDivisionError:
        print('\n\nERROR: Denominator cannot be 0, amend this value to continue')

print()
print()
print(final)