"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""


class NegativeNumericValue(Exception):
    def __init__(self):
        super().__init__()

minutes_remaining_input = input("Minutes remaining until the deadline: ")

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead

invalid = True
while invalid:
    try:
        minutes_remaining = int(minutes_remaining_input)

        if minutes_remaining <= 0:
            raise NegativeNumericValue()

        invalid = False
    except ValueError:
        print('Entr a valid number')
    except NegativeNumericValue:
        print('\nWARNING: Deadline has passed')
        quit()



minute_mod = minutes_remaining % 60

hours = (minutes_remaining-minute_mod) / 60

hour_mod = hours % 24

days = (hours-hour_mod) / 24


print(f'{days:.0f} days, {hour_mod:.0f} hours and {minute_mod:.0f} minutes left until the deadline')


    