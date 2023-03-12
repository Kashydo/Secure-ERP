""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
import fileinput
import sys
import csv
from model import data_manager, util


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
ID = 0
NAME = 1
BIRTH_DAY = 2
DEPARTAMENT = 3
CLERANCE = 4


def add_emplyee_to_data(employee_data, file=DATAFILE):
    with open(file, "a+") as file:
        file.seek(0)
        file.write('\n')
        file.write(employee_data)


def check_if_emloyee_is_in_data(employee_data, file=DATAFILE):
    with open(file, "r") as file:
        if employee_data in file.read():
            return True
        else:
            return False


def get_list_of_employees(file=DATAFILE):
    with open(file, "r") as file:
        employees_list = [line.strip().split(';')for line in file]
    employees_list.insert(0, HEADERS)
    return employees_list


def get_data_of_employee(serched_data, file=DATAFILE):
    with open(file, "r") as file:
        for line in file:
            if serched_data in line:
                return line.strip()


def update_employee_data(employee_id, edited_emplyee_data, file=DATAFILE):
    if check_if_emloyee_is_in_data(employee_id):
        employee = get_data_of_employee(employee_id)
        for line in fileinput.input(file, inplace=1):
            line = line.replace(employee, ';'.join(edited_emplyee_data,))
            sys.stdout.write(line)


def remove_employee_from_data(employee_id, file=DATAFILE):
    with open(file, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            if not line.strip('\n').startswith(employee_id):
                file.write(line)


def get_employees_single_column_in_file(header, file=DATAFILE):
    with open(file, 'r') as file:
        employee_list = get_list_of_employees()
        emplyees_column = [_[header] for _ in employee_list]
        emplyees_column.pop(0)
    return emplyees_column


def get_id_birthday_dictionary():
    employees_id = get_employees_single_column_in_file(ID)
    employees_birthday = get_employees_single_column_in_file(BIRTH_DAY)
    return {employees_id[i]: employees_birthday[i] for i in range(len(employees_id))}


def who_is_oldest_youngest(employees_dictionary, dates_list, min_max):
    year = min_max(dates_list).strftime('%Y-%m-%d')
    return tuple(key + ' ' + get_data_of_employee(key).split(';')[NAME] for key,
                 value in employees_dictionary.items() if value == year)


def count_emplyees_with_at_least_input(input):
    clerance_list = get_employees_single_column_in_file(CLERANCE)
    return sum(int(i) >= int(input) for i in clerance_list)


def count_employees_per_departament():
    employees_in_each_depatament = {}
    departaments_list = get_employees_single_column_in_file(DEPARTAMENT)
    for departament in departaments_list:
        if departament not in employees_in_each_depatament.keys():
            employees_in_each_depatament[departament] = departaments_list.count(
                departament)
    return employees_in_each_depatament
