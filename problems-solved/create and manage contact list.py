contacts=["laksh","rohit","nandini"]
def create():
    create="start with an initial list"
def add():
    contact=input("Enter a contact: ")
    contacts.append(contact)
def modify():
    contact=input("Enter contact to update: ")
    new_contact=input("Enter new name for the contact: ")
    contacts[contacts.index(contact)]= new_contact
def delete():
    contact=input("Enter the contact you want to delete: ")
    contacts.remove(contact)
def filter():
    letter=input("Enter Starting letter of the contact: ")
    for contact in contacts:
        if contact.startswith(letter):
            print(contact)
def search():
    contact=input("Enter contact to search: ")
    if contact in contacts:
        print(contact)
    else:
        print("Contact not found")
def replace():
    contact=input("Enter Contact to replace: ")
    if contact in contacts:
        new_contact=input("Enter New Contact")
        contacts[contacts.index(contact)] = new_contact
    
        
