""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def add_emplyee_to_data(employee_data, file=DATAFILE):
    with open(file, "a+") as file:
        file.write(employee_data)
        file.write('\n')


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
