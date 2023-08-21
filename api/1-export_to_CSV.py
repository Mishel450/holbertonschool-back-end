#!/usr/bin/python3
"""task-1"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    txt = '"{}","{}","{}","{}"\n'
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    task_done = 0
    task_count = 0
    user_id = int(argv[1])
    r_users = requests.get(req.format(user_id)).json()
    r_todos = requests.get(req_all_task).json()
    username_task = r_users['username']
    with open("{}.csv".format(user_id), "w") as file:
        for i in r_todos:
            if i['userId'] == user_id:
                file.write(txt.format(user_id, username_task,
                                      i['completed'], i['title']))
