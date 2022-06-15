def main():
    phone_book = {}
    while True:
        user_command = input()
        if user_command == '.':
            break
        elif user_command.lower() == 'hello':
            print(greeting())
        elif user_command.lower() in ("good bye", "close", "exit"):
            print(good_buy())
            break
        elif user_command.lower().startswith('add '):
            print(add(user_command, phone_book))
        elif user_command.lower().startswith('change '):
            print(change(user_command, phone_book))
        elif user_command.lower() == 'show all':
            print(show_all(phone_book))
        elif user_command.lower().startswith('phone '):
            print(phone(user_command, phone_book))
            

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name do not exist in your phone book!'
        except ValueError:
            return 'Please enter a phone number.'
        except IndexError:
            return 'Give me name and phone please.'
    return inner


def greeting():
    return 'How can I help you?'

def good_buy():
    return 'Good buy!'

def show_all(phones: dict):
    result = ''
    for k, v in phones.items():
        result = result + f'{k} : {v}\n'
    return result[:-1]

@input_error
def add(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = command[1]
    phone_number = command[2]
    phone_book[name] = int(phone_number)
    return 'Done!'


@input_error
def change(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 3:
        raise IndexError()
    name = command[1]
    phone_number = command[2]
    if name not in phone_book:
        raise KeyError()
    phone_book[name] = int(phone_number) 
    return 'Done!'

@input_error
def phone(user_command, phone_book):
    command = user_command.split(' ')
    if len(command) != 2:
        raise KeyError()
    name = command[1]
    return phone_book[name]


if __name__ == "__main__":
    main()