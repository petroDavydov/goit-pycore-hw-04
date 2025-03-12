
# Parser
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Add contact
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Change phone number for existing contact
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Error: Contact {name} does not exist."

# Show phone number for existing contact
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    return f"Error: Contact {name} does not exist."


# Print all contacts
def show_all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts found."


# Main function
def main():

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("You enter wrong/invalid command. Try again ")


if __name__ == "__main__":
    main()
