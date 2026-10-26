
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    if number != -1:
        print(number) 
        countdown(number-1) 


invalid = True
while invalid:
    try:
        number = int(input('Enter a Positive Integer Number: -> '))
        if number < 0:
            print('Enter a positive integer')
        else:
            invalid = False
    except ValueError:
        print('Enter a valid integer')


countdown(number)