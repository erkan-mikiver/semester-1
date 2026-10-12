# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]
k = 1
for i in range(0, L-1):
    a = sequence[i]
    ak = a - k 
    if ak < 0:
        ak = a + k
    elif ak in sequence:
        ak = a + k
    k += 1
    sequence.append(ak)
    
# 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22,
# 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 
# 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79, 
# 113, 78, 114, 77, 39, 78, 38, 79, 37, 80, 
# 36, 81, 35, 82, 34, 83, 33, 84, 32


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence