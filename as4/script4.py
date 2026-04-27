def parse_input(user_input: str) -> tuple:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Error: use 'add [name] [phone]'."
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' to update."
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Error: use 'change [name] [phone]'."
    name, phone = args
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact changed."

def show_phone(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Error: use 'phone [name]'."
    name = args[0]
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]

def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved yet."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()