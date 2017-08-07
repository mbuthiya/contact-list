from contact import Contact

class FavouriteContact(Contact):

    '''
    FavouriteContact class that creates contact objects

    Args:
        Contact: The Contact class which is the parent Class and where we inherit the class behaviours
    '''

    favourite_contacts = []

    def __init__(self,first_name,last_name,phone_number,email,birthday):
        '''
        __init__ method helping us create properties for our objects

        '''
        Contact.__init__(self,first_name,last_name,phone_number,email)
        self.birthday = birthday



    def save_fav_contact(self):
        '''
        save_fav_contact method that saves the FavouriteContact object into a list
        '''

        FavouriteContact.favourite_contacts.append(self)


    def delete_fav_contact(self):
        '''
        delete_fav_contact method that deletes the FavouriteContact object from a list
        '''
        FavouriteContact.favourite_contacts.remove(self)


    @classmethod
    def display_fav_contacts(cls):

        '''
        Class method that returns all the favourite contacts
        '''
        return cls.favourite_contacts
