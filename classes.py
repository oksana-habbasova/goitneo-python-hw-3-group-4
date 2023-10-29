from datetime import datetime
from errors import  NotExistsContactError, PhoneLengthError, NotExistsPhoneError, BirthdayFormatError
from collections import UserDict
from datetime import datetime
from birthdays import get_birthdays_per_week

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise BirthdayFormatError     
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise PhoneLengthError
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = '-'
        self.phones = []

    def __str__(self):
        name = self.name.value
        phones = '; '.join(p.value for p in self.phones)
        birthday = self.birthday
        return f"Contact name: {name}, phones: {phones}, birthday: {birthday}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return 
        raise NotExistsPhoneError
        
    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


class AddressBook(UserDict):
    def add_record(self, record):
       self.data[record.name.value] = record

    def find_record(self, name):
        if not self.data.get(name):
            raise NotExistsContactError
        return self.data[name]
    
    def has_record(self, name):
        if self.data.get(name):
            return True
        return False
    
    def delete_record(self, name):
        if not self.data.get(name):
            raise NotExistsContactError
        del self.data[name]

    def get_birthdays_per_week(self):
        contacts = []

        for record in self.data.values():
            if record.birthday.value:
                user = {
                    "name": record.name.value, 
                    "birthday": datetime.strptime(record.birthday.value, "%d.%m.%Y")
                }
                contacts.append(user)
        
        return get_birthdays_per_week(contacts)