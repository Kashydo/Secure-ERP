from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_menu(title, list_options):
    clear()
    print(f'{title}:')
    for i in range(len(list_options)):
        print(f'({i}) {list_options[i]}')


def print_message(message):
    print(message)
    input("Press Enter to continue...")


def print_general_results(result, label):
    if isinstance(result, dict):
        print(label)
        for key in result:
            print(str(key)+':', str(result[key])+'; ', end='')
        print('')
    elif isinstance(result, list):
        print(label+':')
        for value in result:
            print(value+'; ', end='')
        print('')
    elif isinstance(result, tuple):
        print(label+':')
        for value in result:
            print(value+'; ', end='')
        print('')
    else:
        print(label+':', result)
    input("Press Enter to continue...")


def print_table(table):
    lenght = max(table, key=len)
    for rows in table:
        print(
            ' -------------------------------------------------------------------------------')
        for column in rows:
            print(f'|{(column) :15}', end='')
        print('|')
    print('-------------------------------------------------------------------------------')

    input("Press Enter to continue...")


def get_input(label):
    user_input = input(f"Prosze podac {label}: ")
    return user_input


def get_inputs(labels):
    user_inputs = []
    for label in labels:
        user_inputs.append(input(f"Proszę podać {label}: "))
    return user_inputs


def yes_no_question(action, label):
    yes_no = None
    while yes_no == None:
        user_answer = input(f'Czy chcesz {action} {label}: [T]ak/[N]ie: ')
        if user_answer.lower() == 't':
            yes_no = 1
            return True
        elif user_answer.lower() == 'n':
            yes_no = 0
            return False
        else:
            print_error_message('Proszę wpisać odpowiedź [T]/[N]: ')


def print_error_message(message):
    print(message)
    input("Press Enter to continue...")
