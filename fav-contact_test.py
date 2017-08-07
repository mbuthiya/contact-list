import unittest
from fav_contact import FavouriteContact

class TestFavouriteContact(unittest.TestCase):
    '''
    Test class to test behaviours of the Favourite contact class
    '''

    def setUp(self):

        self.new_fav_contact = FavouriteContact("James","Muriuki","0712345678","james@ms.com")

    def test_init(self):
        '''
        Method to test  if new contact is instanciated correctly
        '''

        self.assertEqual(self.new_fav_contact.first_name,"James")
        self.assertEqual(self.new_fav_contact.last_name,"Muriuki")
        self.assertEqual(self.new_fav_contact.phone_number,"0712345678")
        self.assertEqual(self.new_fav_contact.email,"james@ms.com")

    



if __name__ == "__main__":
    unittest.main()
