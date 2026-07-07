
contact = {}

def Display_contact():
    print("name\n\ncontact book")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choice = int(input(" 1. Add new \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit \n  Enter number (1-6): "))
    if choice == 1:
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        contact[name] = phone
    elif choice == 2:
        search_contact = input("Enter the contact name: ")
        if search_contact in contact:
            print(search_contact, "is contact number", contact[search_contact])
        else:
            print("name is not fund")
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            Display_contact()
    elif choice == 4:
        Edete_contact = input("Enter name contact: ")
        if Edete_contact in contact:
            phone = input("Enter your phone: ")
            contact[Edete_contact] = phone
            print("contact update")
            Display_contact()
        else:
            print("name is not fund")
    elif choice == 5:
        delete_contact = input("Enter name contact to delete")
        if delete_contact in contact:
            confirm = input("Do yuo wont to delete the contact (y-n): ").lower
            if confirm == "y":
                contact.pop(delete_contact)
        else:
            print("name is not fund")
    else:
        break
    print("goodby!")
    
