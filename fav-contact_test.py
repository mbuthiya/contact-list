import unittest
from fav_contact import FavouriteContact
from datetime import date


class TestFavouriteContact(unittest.TestCase):
    '''
    Test class to test behaviours of the Favourite contact class
    '''

    def setUp(self):
        self.birthday = date(date.today().year,4,14)
        self.new_fav_contact = FavouriteContact("James","Muriuki","0712345678","james@ms.com",self.birthday)


    def test_init(self):
        '''
        Method to test  if new contact is instanciated correctly
        '''

        self.assertEqual(self.new_fav_contact.first_name,"James")
        self.assertEqual(self.new_fav_contact.last_name,"Muriuki")
        self.assertEqual(self.new_fav_contact.phone_number,"0712345678")
        self.assertEqual(self.new_fav_contact.email,"james@ms.com")
        self.assertEqual(self.new_fav_contact.birthday.month,4)


    def test_save_fav_contact(self):
        '''
        test_save_fav_contact test to see if a favourite_contact is saved
        '''
        self.new_fav_contact.save_fav_contact()
        self.assertEqual(len(FavouriteContact.favourite_contacts),1)


    def test_delete_fav_contact(self):
        '''
        test_delete_fav_contact test to see if we can delete a favourite contact from our
        list
        '''

        self.new_fav_contact.save_fav_contact()

        test_fav_contact = FavouriteContact("test","user","0711223344","test@user.com",self.birthday)
        test_fav_contact.save_fav_contact()

        self.new_fav_contact.delete_fav_contact()
        self.assertEqual(len(FavouriteContact.favourite_contacts),1)

    


if __name__ == "__main__":
    unittest.main()
