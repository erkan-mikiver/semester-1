# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

        if len(self.pence) == 1:
            x = '0'.join(self.pence)
        else:
            x = self.pence

        return f'£{self.pounds}.{x}'



    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other, Money):
            raise TypeError("Make sure the other parameter is a Money object")

        x = self.pounds + other.self.pounds
        y = self.pence + other.self.pence
        if y >= 100:
            x += 1
            y -= 100
            return Money(x, y)
        else:
            return Money(x, y)
