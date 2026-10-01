"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places

invalid = True
while invalid:
    try:
        travel_cost_input = input("\nTravel cost in pounds: ")
        travel_cost = float(travel_cost_input)
        if travel_cost < 0:
            print('\n\nERROR: Travel Cost cannot be negative')
            continue

        food_cost_input = input("\nFood cost in pounds: ")
        food_cost = float(food_cost_input)
        if food_cost < 0:
            print('\n\nERROR: Food Cost cannot be negative')
            continue
            
        accommodation_cost_input = input("\nAccommodation cost in pounds: ")
        accomodation_cost = float(accommodation_cost_input)
        if accomodation_cost < 0:
            print('\n\nERROR: Accomodation Cost cannot be negative')
            continue

        invalid = False

    except ValueError:
        print('\n\nERROR: Enter a valid numerical value')


total = accomodation_cost + food_cost + travel_cost

print(f'\n\nTotal Cost: £{total:.2f} \nAccomodation Cost: £{accomodation_cost:.2f} \nFood Cost: £{food_cost:.2f} \nTravel Cost: £{travel_cost:.2f}')
    


