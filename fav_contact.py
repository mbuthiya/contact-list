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
        FavouriteContact.favourite_contacts.append(self)
