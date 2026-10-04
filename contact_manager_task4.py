# File Handling Mini Project - Contact Manager

import csv

FILE_NAME = "contacts.csv"

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    try:
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone])
        print("Contact added successfully!")

    except Exception as e:
        print("Error while saving contact:", e)


# Function to view all contacts
def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nContacts:")

            found = False
            for row in reader:
                print("Name:", row[0], "| Phone:", row[1])
                found = True

            if not found:
                print("No contacts found.")

    except FileNotFoundError:
        print("No contact file found.")


# Function to search for a contact
def search_contact():
    search_name = input("Enter name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            found = False

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("Contact found!")
                    print("Name:", row[0])
                    print("Phone:", row[1])
                    found = True

            if not found:
                print("Contact not found.")

    except FileNotFoundError:
        print("No contact file found.")


# Main menu
while True:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
