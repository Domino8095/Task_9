contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide name and phone number."
        except IndexError:
            return "Invalid command format."
    return wrapper

@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added {name} with phone number {phone} to contacts."

@input_error
def change_contact(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone number for {name} to {phone}."
    else:
        raise KeyError

@input_error
def show_phone(command):
    _, name = command.split()
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        raise KeyError

@input_error
def show_all():
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found."

def main():
    while True:
        user_input = input("Enter command: ").lower()
        if user_input.startswith("hello"):
            print("How can I help you?")
        elif user_input.startswith("add"):
            print(add_contact(user_input))
        elif user_input.startswith("change"):
            print(change_contact(user_input))
        elif user_input.startswith("phone"):
            print(show_phone(user_input))
        elif user_input.startswith("show all"):
            print(show_all())
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
