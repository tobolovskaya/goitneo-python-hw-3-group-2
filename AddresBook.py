import pickle
import re
from datetime import datetime


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, number):
        if not re.match(r"^\d{10}$", number):
            raise ValueError("Phone number must have 10 digits.")
        self.number = number


class Birthday(Field):
    def __init__(self, birthday_str):
        try:
            self.date = datetime.strptime(birthday_str, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid birthday format. Use DD.MM.YYYY.")


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.birthday = Birthday(birthday) if birthday else None


class AddressBook:
    records = {}

    def add_record(self, name, phone=None, birthday=None):
        if name in self.records:
            return "Contact already exists."
        self.records[name] = Record(name, phone, birthday)
        return f"Added {name}."

    def save_to_disk(self, filename="address_book.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.records, file)
        return "Address book saved."

    def load_from_disk(self, filename="address_book.pkl"):
        try:
            with open(filename, "rb") as file:
                self.records = pickle.load(file)
            return "Address book loaded."
        except FileNotFoundError:
            return "Address book file not found. Starting with an empty address book."


def command_handler(command, book, *args):
    if command == "add":
        try:
            return add_contact(book, *args)
        except ValueError as e:
            return str(e)


def add_contact(book, name, phone=None, birthday=None):
    try:
        return book.add_record(name, phone, birthday)
    except ValueError as e:
        return str(e)


def main():
    book = AddressBook()
    print(book.load_from_disk())  # Load book from disk on startup

    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command.lower() in ["close", "exit"]:
            print("Good bye!")
            break

        print(command_handler(command.lower(), book, *args))


if __name__ == "__main__":
    main()
