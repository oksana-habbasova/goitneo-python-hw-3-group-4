class NoContactsError(Exception):
    pass

class NotExistsContactError(Exception):
    pass

class PhoneLengthError(Exception):
    pass

class NotExistsPhoneError(Exception):
    pass

class BirthdayFormatError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoContactsError:
            print('There are no saved contacts yet')
        except NotExistsContactError:
            print('A contact with this name does not exists')
        except PhoneLengthError:
            print('Enter 10 digits phone number')
        except NotExistsPhoneError:
            print('A contact with this phone does not exists')
        except BirthdayFormatError:
            print('Enter your birthday in DD.MM.YYYY format please')
        except BirthdayFormatError:
            print('Enter your birthday in DD.MM.YYYY format please')
        except ValueError:
            print('Enter user name and data please')
        except KeyError:
            print('There is no contact with this name')
        except IndexError:
            print('Enter user name please')
        except AttributeError:
            print('There is no such a data')
        
    return inner