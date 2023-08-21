#!/usr/bin/python3
"""task-0"""
import requests
from sys import argv

if __name__ == "__main__":
    txt1 = "Employee {} is done with tasks({}/{}):"
    txt2 = "    {}"
    r = requests.get(argv[1])
    print(txt1.format(r['EMPLOYEE_NAME'], r['NUMBER_OF_DONE_TASKS'],
                      r['TOTAL_NUMBER_OF_TASKS']))
    print(txt2.format(r['TASK_TITLE']))
