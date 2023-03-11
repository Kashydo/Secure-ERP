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
import os
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
