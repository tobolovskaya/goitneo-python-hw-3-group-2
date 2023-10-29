def parse_input(user_input):
    cmd, *args = user_input.split(" ")
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    try:
        if contacts[name]:
            contacts[name] = phone
            return "Contact changed."
    except KeyError:
        contacts[name] = phone
        return "Contact added."


def get_phone(args, contacts):
    name = args[0]
    try:
        if contacts[name]:
            return contacts[name]
    except KeyError:
        return "Contact not found."


def get_all(contacts):
    print(f"{'_'*73}")
    print(f"|{'Name:':^40}|{'Phone:':^30}|")
    print(f"|{'_'*40}|{'_'*30}|")
    if len(contacts) > 0:
        for k, v in contacts.items():
            print(f"|{k:^40}|{v:^30}|")
            print(f"|{'_'*40}|{'_'*30}|")
    else:
        print(f"|{' '*71}|")
        print(f"|{'No records found. Add at first':^71}|")
        print(f"|{'_'*71}|")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            get_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
