#!virtual/bin/python3.6

from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    return new_contact = Contact(fname,lname,phone,email)


def save_contact(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def delete_contact(contact,contact_list):
    '''
    Function to delete a contact
    '''

    contact.delete_contact()
