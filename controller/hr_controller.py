from model import util
from model.hr import hr as hr
from view import terminal as view
import datetime
ID = 0
NAME = 1
BIRTH_DAY = 2
DEPARTAMENT = 3
CLERANCE = 4

# sends to model to open list of employees
# sends information to view to print


def list_employees():
    list_of_employees = hr.get_list_of_employees()
    view.print_table(list_of_employees)


def check_if_name_correct(name):
    return name.replace(' ', '').isalpha()


def check_if_date_correct(date, data_format='%Y-%m-%d'):
    try:
        datetime.datetime.strptime(date, data_format)
    except:
        return False
    return True


def check_if_clerance_correct(clerance, start=0, finish=7):
    try:
        int(clerance)
    except:
        return False
    if start <= int(clerance) <= finish:
        return True
    else:
        return False


def check_if_employee_data_corect(data, partametrs_to_check=[NAME, BIRTH_DAY, CLERANCE], messeges=['imie i nazwisko', 'data urodzenia', 'poziom dostepu'], functions_list=[check_if_name_correct, check_if_date_correct, check_if_clerance_correct]):
    for function, parametr, messege in zip(functions_list, partametrs_to_check, messeges):
        while function(data[parametr]) == False:
            view.print_error_message(
                f'Podane dane " {messege} " są nie prawidłowe')
            data[parametr] = view.get_input(messege)
    return data


def add_employee(employee=['imię i nazwisko', 'data urodzenia (YYYY-MM-DD)',
                           'departament', 'poziom dostepu']):

    EMPLOYEE = view.get_inputs(employee)
    EMPLOYEE.insert(0, 'ID')
    check_if_employee_data_corect(EMPLOYEE)
    employee_to_add = [EMPLOYEE[NAME], EMPLOYEE[BIRTH_DAY],
                       EMPLOYEE[DEPARTAMENT], EMPLOYEE[CLERANCE]]
    if hr.check_if_emloyee_is_in_data(';'.join(employee_to_add)):
        view.print_error_message(
            'Pracownik odpowiadający tym danym już jest w bazie')
    else:
        EMPLOYEE[ID] = util.generate_id()
        hr.add_emplyee_to_data(';'.join(EMPLOYEE))
        view.print_message(
            f'Pracownik {EMPLOYEE} został dodany do bazy danych')


def update_employee():
    employee_id = view.get_input('ID pracownika')
    if hr.check_if_emloyee_is_in_data(employee_id):
        employee = hr.get_data_of_employee(employee_id).split(';')
        view.print_general_results(employee, 'Pracownik')
        updated_employee = chenging_chosen_data('zmienić', employee)
        view.print_general_results(employee, 'Pracownik')
        hr.update_employee_data(employee_id, updated_employee)
    else:
        view.print_message('Nie ma praconika o tym ID')


def chenging_chosen_data(employee_data,  messeges=['imie i nazwisko', 'data urodzenia', 'departament', 'poziom dostepu']):
    for employee_info, messege in zip(range(1, 5), messeges):
        if view.yes_no_question(messege):
            employee_data[employee_info] = view.get_input(messege)
        else:
            pass
    return employee_data


def delete_employee():
    employee_id = view.get_input('ID pracownika')
    if hr.check_if_emloyee_is_in_data(employee_id):
        employee = hr.get_data_of_employee(employee_id).split(';')
        view.print_general_results(employee, 'Pracownik')
        if view.yes_no_question('usunąć', 'pracownika'):
            hr.remove_employee_from_data(employee_id)
            view.print_message(f'{employee[NAME]} został/a usunięty/a')


def get_oldest_and_youngest():
    employees = hr.get_id_birthday_dictionary()
    dates = []
    for key in employees:
        dates.append(datetime.datetime.strptime(
            employees[key], '%Y-%m-%d'))
    oldest_employees = hr.who_is_oldest_youngest(employees, dates, min)
    youngest_employees = hr.who_is_oldest_youngest(employees, dates, max)
    view.print_general_results(oldest_employees, 'Najstarsi pracownicy to')
    view.print_general_results(youngest_employees, 'Najmłodsi pracownicy to')


def get_average_age():
    employees_birthday = hr.get_employees_birthday()
    today = datetime.datetime.today()
    sum_ages = sum((
        today - datetime.datetime.strptime(birthday, '%Y-%m-%d') for birthday in employees_birthday),  datetime.timedelta(0))
    avarage_age = (sum_ages / len(employees_birthday)/365).days
    view.print_general_results(avarage_age, 'Średnia wieku pracowników to')


def check_if_date_in_range(date, future_date):
    employees = hr.get_id_birthday_dictionary()
    closest_birthday = {}
    for key in employees:
        emplee_birthday = employees[key][5:]
        if date <= datetime.datetime.strptime(emplee_birthday, '%m-%d') <= future_date:
            closest_birthday[key + ' ' +
                             hr.get_data_of_employee(key).split(';')[NAME]] = emplee_birthday
    return closest_birthday


def next_birthdays():
    is_date_correct = False
    while is_date_correct == False:
        inputed_date = view.get_input('datę (MM-DD)')
        is_date_correct = check_if_date_correct(
            inputed_date, data_format='%m-%d')
    date = datetime.datetime.strptime(
        inputed_date, '%m-%d')
    future_date = date + datetime.timedelta(days=14)
    closest_birthday = check_if_date_in_range(date, future_date)
    if not closest_birthday:
        view.print_message('Nikt nie bedzię obchodzić urodzin')
    else:
        view.print_general_results(
            closest_birthday, 'Urodziny w ciągu 14 dni od podanej daty obchodzą')


def count_employees_with_clearance():
    inputed_clerance = view.get_input('poziom dostępu')
    clerance_count = hr.count_hom_many_emplyees_with_input(inputed_clerance)
    view.print_general_results(
        clerance_count, 'Pracowników z co najmniej podanym poziomem dostępu jest')


def count_employees_per_department():
    employees_in_departaments = hr.count_employees_per_departament()
    view.print_general_results(
        employees_in_departaments, 'Pracownicy w działach')


count_employees_per_department()


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
