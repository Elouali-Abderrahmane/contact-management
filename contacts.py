message = """

Contact Management

1- Add a contact
2- View contacts
3- Edit a contact
4- Exit

"""

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    # Get a valid contact ID (numeric only)
    while True:
        id = input("Enter the contact ID: ").strip()
        if id.isdigit():
            break
        else:
            print("The ID should contain only numbers")
    
    # Get the contact name
    name = input("Please type a name: ").strip().title()
    
    # Get a valid phone number (9 digits after +212 )
    while True:
        phone = input("Please type a phone number (9 digits after +212 ): +212 ").strip()
        if phone.isdigit() and len(phone) == 9:
            break
        else:
            print("Phone number should contain only numbers and be 9 digits long")

    # Store the contact details in the dictionary
    contacts[id] = {
        "ID": id,
        "name": name,
        "phone": f"+212 6{phone[:3]}-{phone[3:]}",
    }
    print(f"{name} was added successfully...")

# Function to view all contacts
def view_contacts():
    if len(contacts) == 0:
        print("There are no contacts added yet.")
        return
    
    # Print each contact
    for contact in contacts.values():
        print(contact)

# Function to edit a contact
def edit_contact():
    # Get the ID of the contact to edit
    user_id = input("Please enter an ID to edit: ").strip()
    
    # Check if the contact exists
    if user_id in contacts:
        # Get the new name
        new_name = input("Enter a new name: ").strip().capitalize()
        contacts[user_id]["name"] = new_name
        
        # Check if the user wants to change the phone number
        change_phone = input("Do you want to change the phone number as well? (Yes/No): ").strip().lower()
        if change_phone in ["no", "n"]:
            print("Success...")
            return
        
        # Get a valid new phone number
        while True:
            new_phone = input("Enter a new phone number (8 digits after +212 6): +212 6").strip()
            if new_phone.isdigit() and len(new_phone) == 8:
                contacts[user_id]["phone"] = f"+212 6{new_phone[:3]}-{new_phone[3:]}"
                break
            else:
                print("Phone number should contain only numbers and be 8 digits long")
        print("Success...")
    else:
        print("Sorry, there is no contact with the ID you entered.")

# Main function to display the menu and handle user input
def main():
    while True:
        try:
            # Display the menu
            print(message)
            
            # Get the user's choice
            choice = int(input("Please choose a number from 1-4: "))
            
            # Handle the user's choice
            if choice == 4:
                print("Exiting the Program...")
                break
            elif choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                edit_contact()
            else:
                print("Invalid Input. You should enter a number between 1 and 4.")
        except ValueError:
            print("Wrong Input. You must enter a number.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
