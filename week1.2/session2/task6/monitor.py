# Week 1.2, Session 2: Task 6
import sys

temp = int(input("Enter the machine's temperature in degrees Celcius: -> "))
psi = int(input("Enter the machine's pressure in PSI: -> "))
operational = int(input("Provide the machine's operating status (1 for on, 0 for off)"))

unsafe = False



if operational == 1:
    if temp > 80:
        unsafe = True
        print('Temperature is too high! Machine shut down is recommended')
    elif temp >= 50 or temp <= 80:
        print('Temperature is within safe limits')
    elif temp < 50:
        print('Tmperature is low, no action needed')

    if psi > 100:
        unsafe = True
        print("Pressure is too high! Machine maintanence recommended")
    elif psi >= 70 or psi <= 100:
        print('Pressure is stable')
    elif psi < 70:
        print('Pressure is low, system is operating normally')
else:
    print("Machine is currently stopped, no immediate action is needed ")

if unsafe:
    print('\nThe machine is currently running in unsafe conditions, a machine shutdown is recommended')