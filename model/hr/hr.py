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
    with open(file, "a+") as emplpyee_list:
        emplpyee_list.write(employee_data)


def check_if_emloyee_is_in_data(employee_data, file=DATAFILE):
    with open(file, "r") as employee_list:
        if employee_data in employee_list.read():
            return True
        else:
            return False
