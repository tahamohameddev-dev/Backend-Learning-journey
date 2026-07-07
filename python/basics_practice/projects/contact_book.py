
# create a contact book use python

contact = {}

def desplay_contact():
    print("name\t\tcontact book")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display Contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit \n Enter nomder (1-6): "))
    if choice == 1:
        name = input("Enter your name: ")
        phone = input("Enter your phonr: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"is contact number", contact[search_name])
        else:
            print("Name is not fund contact book")
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            desplay_contact()
    elif choice == 4:
        Edete_contact = input("Enter yuor name contact: ")
        if Edete_contact in contact:
            phone = input("Enter your phone: ")
            contact[Edete_contact] = phone
            print("Contact updated")
            desplay_contact()
        else:
            print("name is fund contact")
    elif choice == 5:
        delete_contact = input("Enter your name contact to delete: ")
        if delete_contact in contact:
            confirm = input("Do you wont to delete thes contact y/n: ")
            if confirm == 'y' or 'Y':
                contact.pop(delete_contact)
                desplay_contact()
        else:
            print("name is not fund in contact book")
    else:
        break