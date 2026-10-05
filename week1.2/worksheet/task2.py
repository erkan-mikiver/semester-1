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
    list_len = len(numbers)

    if list_len == 2:
        median = (sum(numbers) / 2)
    elif (list_len % 2) == 0:
        middle = (list_len + 1) / 2
        x = numbers[int((middle-0.5)-1)] + numbers[int((middle+0.5) - 1)]
        median = x / 2
    else:
        middle = ((list_len + 1) / 2) -1
        median = numbers[middle]

    # MEAN
    total = sum(numbers)

    mean = total / (list_len)

    # MAX
    maximum = max(numbers)

    # MIN
    minimum = min(numbers)

    print(f"Minimum = {minimum}")
    print(f"Maximum = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")

