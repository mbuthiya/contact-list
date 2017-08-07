class Contact:
    """
    Contact class that creates contact objects.
    """

    contact_list = [] # Empty contact list


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


    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)


    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        found_contact = [contact for contact in cls.contact_list if contact.phone_number == number ]

        return found_contact[0]

    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        found_contact = [contact for contact in cls.contact_list if contact.phone_number == number ]

        if len(found_contact) > 0:
            return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
