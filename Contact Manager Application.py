# Contact Manager Application in Python

# Initialize an empty contact list
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully.")

# Function to display all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

# Function to search for a contact by name or phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == search_term or contact['phone'] == search_term:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

# Function to update an existing contact
def update_contact():
    search_term = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == search_term:
            print("Updating contact details. Leave blank to keep current value.")
            contact['name'] = input(f"Name [{contact['name']}]: ") or contact['name']
            contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'] == search_term:
            del contacts[i]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Main function to run the contact manager
def main():
    print("Welcome to the Contact Manager!")
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
