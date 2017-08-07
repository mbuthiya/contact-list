#!virtual/bin/python3.6

from contact import Contact
from fav_contact import FavouriteContact

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    return new_contact = Contact(fname,lname,phone,email)



def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()


def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()


def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)


def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.check_existing(number)


def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_all_contacts()

def make_fav_contact(contact,birthday):
    '''
    Function to create a new favourite contact object
    '''

    return new_fav_contact = FavouriteContact(contact.first_name,contact.last_name,contact.phone_number,contact.email,birthday)

def save_favourite_contact(fav_contact):
    '''
    Function to save a favourite contact
    '''
    fav_contact.save_fav_contact()


def delete_favourite_contact(fav_contact):
    '''
    Function to delete a favourite contact
    '''
    fav_contact.delete_fav_contact()

def display_favourite_contacts():

    '''
    Function that displays all the favourite contacts
    '''

    return FavouriteContact.display_fav_contacts()
