phone_book = {}

while True:
    print("==== MY PHONE BOOK ====")

    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contacts")
    print("4. Delete contact")
    print("Exit")

    choice = input("Enter your chioce: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        phone_book[name] = phone

        print("Contact added successfully")


    elif choice == "2":
        if not phone_book:
            print("Phone book is empty")
        else:
            for name, phone in phone_book.items():
                print(name, phone)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found")
        
    elif choice == "5":
        print("5. Goodby")
        break

    else:
        print("Invalid Choice")