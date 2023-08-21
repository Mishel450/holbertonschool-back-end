#!/usr/bin/python3
"""task-0"""
import requests
from sys import argv

if __name__ == "__main__":
    txt1 = "Employee {} is done with tasks({}/{}):"
    txt2 = "\t {}"
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    task_done = 0
    task_count = 0
    id = int(argv[1])
    r_users = requests.get(req.format(id)).json()
    r_todos = requests.get(req_all_task).json()
    for i in r_todos:
        if i['userId'] == id:
            task_count += 1
        if i['userId'] == id and i['completed'] is True:
            task_done += 1
    print(txt1.format(r_users['name'], task_done,
                      task_count))
    for i in r_todos:
        if i['userId'] == id and i['completed'] is True:
            print(txt2.format(i['title']))
