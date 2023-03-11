def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    pass


def print_message(message):
    print(message)
    # # """Prints a single message to the terminal.

    # # Args:
    # #     message: str - the message
    # # """
    # pass


def print_general_results(result, label):
    if isinstance(result, dict):
        print(label)
        for key, value in result:
            print(key+':', value+'; ', end='')
        print('')
    elif isinstance(result, list or tuple):
        print(label+':')
        for value in result:
            print(value+'; ', end='')
        print('')
    else:
        print(label+':', value)

    # """Prints out any type of non-tabular data.
    # It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    # lists/tuples (like "@label: \n  @item1; @item2"),
    # and dictionaries
    # (like "@label \n  @key1: @value1; @key2: @value2")
    # """
    # pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    print('/------------------------------------------------------------------------------------\\')
    for rows in table:
        print('|', end='')
        for column in rows:
            print(f'{column :15}', "|", end='')
        print('\n------------------------------------------------------------------------------------')


# """Prints tabular data like above.

# Args:
#     table: list of lists - the table to print out
# """
# pass


def get_input(label):
    user_input = input(f"Prosze podac {label}: ")
    return user_input
    # """Gets single string input from the user.

    # Args:
    #     label: str - the label before the user prompt
    # """
    # pass


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

# """Gets a list of string inputs from the user.

# Args:
#     labels: list - the list of the labels to be displayed before each prompt
# """
# pass


def print_error_message(message):
    print(message)
    # """Prints an error message to the terminal.

    # Args:
    # #     message: str - the error message
    # # """
    # # pass
