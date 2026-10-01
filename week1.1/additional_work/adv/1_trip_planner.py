"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""


class NegativeNumericValue(Exception):
    def __init__(self):
        super().__init__()

destination = input("Where are you going to? ")

# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative value

invalid = True
while invalid:
    try:
        distance_miles_input = input("\n\nHow many miles will you travel? ")
        distance_miles = int(distance_miles_input)

        time_hours_input = input("\nHow many hours will the journey take? ")
        time_hours = int(time_hours_input)

        if distance_miles <= 0 or time_hours <= 0:
            raise NegativeNumericValue()

        invalid = False
        
    except ValueError:
        print('\nPlease enter a valid numerical amount')
    except NegativeNumericValue:
        print('\nInvalid Numerical Value Entered - Please enter non zero/negative values')


avg_speed = (distance_miles/time_hours)

print(f'Destination: {destination} \nDistance to travel: {distance_miles} miles \nAverage Speed: {avg_speed:.2f} mph')
        
