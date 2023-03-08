from model import util
from model.hr import hr as hr
from view import terminal as view
import datetime
ID = 0
NAME = 1
BIRTH_DAY = 2
DEPARTAMENT = 3
CLERANCE = 4
data_format = '%Y-%m-%d'

# sends to model to open list of employees
# sends information to view to print


def list_employees():

    view.print_error_message("Not implemented yet.")


def add_employee(employee=['imię i nazwisko', 'data urodzenia (YYYY-MM-DD)',
                           'departament', 'poziom dostepu']):

    EMPLOYEE = view.get_inputs(employee)
    EMPLOYEE.insert(0, 'ID')
    date = False
    while EMPLOYEE[NAME].replace(' ', '').isalpha() == False:
        view.print_error_message('Podane imie jest nie prawidłowe')
        EMPLOYEE[NAME] = view.get_input('imię i nazwisko')
    EMPLOYEE[NAME] = EMPLOYEE[NAME].title()
    while date == False:
        try:
            datetime.datetime.strptime(EMPLOYEE[BIRTH_DAY], data_format)
        except:
            view.print_error_message('Podane data jest nieprawidłowa')
            EMPLOYEE[BIRTH_DAY] = view.get_input('datę urodzenia YYYY-MM-DD')
        date = True
    while 7 < int(EMPLOYEE[CLERANCE]) or int(EMPLOYEE[CLERANCE]) < 0:
        view.print_error_message('Podany poziom dostępu jest nieprawidłowy')
        EMPLOYEE[CLERANCE] = view.get_input('poziom dostępu')
    employee_to_add = [EMPLOYEE[NAME], EMPLOYEE[BIRTH_DAY],
                       EMPLOYEE[DEPARTAMENT], EMPLOYEE[CLERANCE]]
    if hr.check_if_emloyee_is_in_data(';'.join(employee_to_add)):
        view.print_error_message(
            'Pracownik odpowiadający tym danym już jest w bazie')
    else:
        EMPLOYEE[ID] = util.generate_id()
        hr.add_emplyee_to_data(';'.join(EMPLOYEE))

    # view.print_error_message("Not implemented yet.")


add_employee()


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
