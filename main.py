from errors import input_error, NoContactsError
from classes import Record, AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, adress_book):
    name, phone = args
    record = Record(name)

    if adress_book.has_record(name):
        record = adress_book.find_record(name)

    record.add_phone(phone)
    adress_book.add_record(record)
    print('Phone added') 

@input_error
def delete_contact(args, adress_book):
    name = args[0]
    adress_book.delete_record(name)
    print('Contact deleted')

@input_error
def change_contact(args, adress_book):
    name, phone, new_phone = args
    record = adress_book.find_record(name)
    record.edit_phone(phone, new_phone)
    print('Contact changed')

@input_error
def get_phone(args, adress_book):
    name = args[0]
    record =  adress_book.find_record(name)
    phones = '; '.join(p.value for p in record.phones)
    print(f"Phones by name {name}: {phones}")

@input_error
def delete_phone(args, adress_book):
    name, phone = args
    record = adress_book.find_record(name)
    record.delete_phone(phone)
    print('Phone deleted')

@input_error
def get_contacts(adress_book):
    if len(adress_book.data) == 0:
        raise NoContactsError
    for record in adress_book.data.values():
        print(record)

@input_error
def add_birthday(args, adress_book):
    name, birthday = args
    record = Record(name)

    if adress_book.has_record(name):
        record = adress_book.find_record(name)

    record.add_birthday(birthday)
    adress_book.add_record(record)
    print('Birthday added') 

@input_error
def show_birthday(args, adress_book):
    name = args[0]
    record =  adress_book.find_record(name)
    birthday = record.birthday.value
    print(f"{name}'s birthday : {birthday}")

@input_error
def get_birthdays_per_week(adress_book):
    if len(adress_book.data) == 0:
        raise NoContactsError
    print(adress_book.get_birthdays_per_week())
   

def main():
    adress_book = AddressBook()

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')

        if user_input == '':
            print('Enter a command please')
            continue

        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            add_contact(args, adress_book)
        elif command == 'change':
            change_contact(args, adress_book)
        elif command == 'delete':
            delete_contact(args, adress_book)
        elif command == 'delete-phone':
            delete_phone(args, adress_book)
        elif command == 'phone':
            get_phone(args, adress_book)
        elif command == 'all':
            get_contacts(adress_book)
        elif command == 'add-birthday':
            add_birthday(args, adress_book)
        elif command == 'show-birthday':
            show_birthday(args, adress_book)
        elif command == 'birthdays':
            get_birthdays_per_week(adress_book)
        else:
            print('Invalid command.')

main()