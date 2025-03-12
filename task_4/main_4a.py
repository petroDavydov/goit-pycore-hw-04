# """"Написаний попередньо код(main_4.py) був запропонований для аналізу 
# Copilot з пропозицією вдосконалити та пояснити виправлення
# """


# import sys

# # Dictionary contacts
# contacts = {}


# def parse_input(user_input):
#     """Parser of command."""
#     parts = user_input.strip().lower().split(maxsplit=2)
#     command = parts[0]
#     args = parts[1:] if len(parts) > 1 else []
#     return command, args


# def add_contact(name, phone):
#     """Add Contacts."""
#     if name in contacts:
#         return f"Contact '{name}' already exists."
#     contacts[name] = phone
#     return f"Contact '{name}' added."


# def change_contact(name, phone):
#     """Change phone number contacts."""
#     if name not in contacts:
#         return f"Contact '{name}' not found."
#     contacts[name] = phone
#     return f"Contact '{name}' updated."


# def show_phone(name):
#     """Shows the phone number for a specific contact."""
#     if name not in contacts:
#         return f"Contact '{name}' not found."
#     return f"Phone number for '{name}': {contacts[name]}"


# def show_all():
#     """Показує всі контакти."""
#     if not contacts:
#         return "No contacts available."
#     return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# def main():
#     """Основна функція."""
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, args = parse_input(user_input)

#         # Вихід із програми
#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break

#         # Обробка команд
#         if command == "hello":
#             print("How can I help you?")
#         elif command == "add" and len(args) == 2:
#             name, phone = args
#             print(add_contact(name, phone))
#         elif command == "change" and len(args) == 2:
#             name, phone = args
#             print(change_contact(name, phone))
#         elif command == "phone" and len(args) == 1:
#             name = args[0]
#             print(show_phone(name))
#         elif command == "all":
#             print(show_all())
#         else:
#             print(
#                 "Invalid command. Please try again, when entered use: add Username Phonenumber")


# if __name__ == "__main__":
#     main()
