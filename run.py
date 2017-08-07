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

def delete_contact(contact):
    '''
    Function to delete a contact
    '''

    contact.delete_contact()

def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''

    found_contact = Contact.find_by_number(number)
    return found_contact
