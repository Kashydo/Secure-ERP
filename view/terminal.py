from os import system, name
import os
import time


RESET = "\033[0;0m"
RED = '\033[31m'
BLUE = '\033[34m'


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def print_menu(title, list_options):
    print(f"{BLUE}{title}:{RESET}\n")
    for i in range(0, len(list_options)):
        if i != 0:
            print(f"{RED}({i}){RESET} {list_options[i]}")
    for i in range(0, len(list_options)):
        if i == 0:
            print(f"{RED}({i}){RESET} {list_options[i]}")
    print()


def print_message(message):
    print(f"{RED}{message}{RESET}\n")


def print_general_results(result, label):
    if type(result) == int:
        print(f"{label}:\n\n{result}")
    elif type(result) == float:
        print(f"{label}:\n\n{format(result, '.2f')}")
    elif type(result) == list:
        print(f"{label}:")
        print()
        for i in result:
            print(f"{i}")
    elif type(result) == tuple:
        result = list(result)
        print(f"{label}:")
        print()
        for i in result:
            print(f"{i}")
    elif type(result) == dict:
        print(f"{label}:")
        print()
        for key, value in result.items():
            print(f"{key}: {value}")
    input("")


def print_table(table):
    separator = " | "
    line_separator = "-"*31
    content = ""
    for row in table:
        line = ""
        for item in row:
            if item != row[-1]:
                line += f"{separator[1:]}{item:^30}"
            else:
                line += f"{separator[1:]}{item:^30}{separator[:-1]}"
        if row != table[-1]:
            content += f"{BLUE}{line}\n{RESET}"
            content += f"{RED}{('|'+line_separator)*len(table[0])}{RESET}"
            content += f"{RED}{'-|'}\n{RESET}"
        else:
            content = f"{content}{BLUE}{line}{RESET}"
    print(f"{RED}/{'-'*(len(line)-2)}\\{RESET}")
    print(f"{RED}{content}{RESET}")
    print(f"{BLUE}\\{'-'*(len(line)-2)}/{RESET}")
    input("")


def get_input(label):
    user_input = input(f"{RED}Prosze podac {label}: {RESET}\n- ")
    clear(0)
    return user_input


def get_inputs(labels):
    user_inputs = []
    for label in labels:
        user_inputs.append(input(f"{RED}Proszę podać {label}: {RESET}\n- "))
    clear(0)
    return user_inputs


def yes_no_question(action, label):
    yes_no = None
    while yes_no == None:
        print('')
        user_answer = input(f'Czy chcesz {action} {label}: [T]ak/[N]ie: ')
        if user_answer.lower() == 't':
            yes_no = 1
            return True
        elif user_answer.lower() == 'n':
            yes_no = 0
            return False
        else:
            print_error_message('Proszę wpisać odpowiedź [T]/[N]: ')
        print('')


def print_error_message(message):
    print(f"Error: {message}\n")
