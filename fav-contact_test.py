import unittest
from fav_contact import FavouriteContact



class TestFavouriteContact(unittest.TestCase):
    '''
    Test class to test behaviours of the Favourite contact class
    '''

    def setUp(self):

        self.new_fav_contact = FavouriteContact("James","Muriuki","0712345678","james@ms.com","Jimbo")


    def tearDown(self):
        '''
        tearDown method that clears the favourite_contacts list
        '''
        FavouriteContact.favourite_contacts = []

    def test_init(self):
        '''
        Method to test  if new contact is instanciated correctly
        '''

        self.assertEqual(self.new_fav_contact.first_name,"James")
        self.assertEqual(self.new_fav_contact.last_name,"Muriuki")
        self.assertEqual(self.new_fav_contact.phone_number,"0712345678")
        self.assertEqual(self.new_fav_contact.email,"james@ms.com")
        self.assertEqual(self.new_fav_contact.nickname,"Jimbo")


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

        test_fav_contact = FavouriteContact("test","user","0711223344","test@user.com","Jimbo")
        test_fav_contact.save_fav_contact()

        self.new_fav_contact.delete_fav_contact()
        self.assertEqual(len(FavouriteContact.favourite_contacts),1)



    def test_display_all_fav_contats(self):
        '''
        Test case tocheck if we can display all the favourite_contacts
        '''

        self.assertEqual(FavouriteContact.display_fav_contacts(),FavouriteContact.favourite_contacts)


if __name__ == "__main__":
    unittest.main()
