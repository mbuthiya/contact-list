class Contact:
    """
    Contact class that creates contact objects.
    """
    def __init__(self,first_name,last_name,phone_number,email):
        '''
        __init__ method that helps us create properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            phone_number: New contact phone number.
            email : New contact email address.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
