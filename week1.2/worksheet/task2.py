# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit('Error: no numbers provided')
else:

    print(numbers)
    # MEDIAN 
    numbers.sort()
    list_len = len(numbers) - 1
    print(list_len)
    if list_len+1 % 2 == 0:
        middle = int(list_len / 2)
        total_mid = sum(numbers[middle:middle+1])
        median = total_mid / 2
    else:
        middle = int((list_len + 1) / 2)
        median = numbers[middle]

    # MEAN
    total = sum(numbers)

    mean = total / (list_len+1)

    # MAX
    maximum = max(numbers)

    # MIN
    minimum = min(numbers)

    print(f"Minimum = {minimum}")
    print(f"Maximum = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")

