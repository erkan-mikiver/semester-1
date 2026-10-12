"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Erkan Mikiver
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input('Enter the number of steps required'))  # read an integer number of steps (>0)

state = "red"

statelist = list(states)
statelen = len(states)
timepassed = 0
i = 0

for _ in range(systime, maxtime+1):

    print(f"Time {systime:03} State {state}")

    systime += 1
    timepassed += 1

    if states[state] == timepassed:
        i += 1
        if i == statelen:
            i = 0
        state = statelist[i]
        timepassed = 0
            
            
    
        


# print time and state y
# increment systime y
# keep count of timepassed y
# when timepassed matches value of key in dict, go to next state in list
# reset timepassed
# at the end of the list, go to the beginning of the dictionary again

    
    

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14