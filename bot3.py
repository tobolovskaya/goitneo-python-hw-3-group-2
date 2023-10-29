import pickle
import re
from datetime import datetime, timedelta


class Phone:
    def __init__(self, number):
        if not re.match(r"^\d{10}$", number):
            raise ValueError("Phone number must have 10 digits.")
        self.number = number


class Birthday:
    def __init__(self, birthday_str):
        try:
            self.date = datetime.strptime(birthday_str, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid birthday format. Use DD.MM.YYYY.")


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = [Phone(phone)] if phone else []
        self.birthday = Birthday(birthday) if birthday else None

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)


class AddressBook:
    def save_to_disk(self, filename="address_book.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)
        return "Address book saved."

    def load_from_disk(self, filename="address_book.pkl"):
        try:
            with open(filename, "rb") as file:
                self.data = pickle.load(file)
            return "Address book loaded."
        except FileNotFoundError:
            return "Address book file not found. Starting with an empty address book."


# Command handling functions ...


def main():
    book = AddressBook()
    print(book.load_from_disk())  # Load book from disk on startup

    # ... remaining part of your bot's main loop ...


if __name__ == "__main__":
    main()
