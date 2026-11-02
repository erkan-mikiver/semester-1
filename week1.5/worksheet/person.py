# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, dob):
        """
        Creates a Person with a name and a date of birth.
        """
        if type(name) is not str:
                    raise TypeError
        elif name == '':
            raise ValueError
                
        if type(dob) is not date:
             raise TypeError
        
        self.name = name
        self.dob = dob

    def initials(self):
        """
            Returns the initials of the Person.
        """
        space = True
        initials = []
        for i in self.name:
            if space:
                initials.append(i.upper())
                space = False
            if i.isalpha() == False:
                space = True
        return ''.join(initials)

    def is_birthday(self):
        """
            Compares today's date to the Person's date of birth.
        """
        today = date.today()
        if self.dob == today:
                return True
        else:
                return False
  
    

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
