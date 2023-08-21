#!/usr/bin/python3
"""task-2"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    txt = '"{}","{}","{}","{}"\n'
    req = "https://jsonplaceholder.typicode.com/users"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    task_done = 0
    task_count = 0

    r_users = requests.get(req).json()
    r_todos = requests.get(req_all_task).json()
    the_list = []
    dict_to_add = {}
    with open("todo_all_employees.json", "w") as file:
        for j in r_users:
            user_id = int(j['id'])
            for i in r_todos:
                if i["userId"] == user_id:
                    the_list.append({
                        "task": i['title'],
                        "completed": i["completed"],
                        "username": j['username']
                    })
            dict_to_add[str(user_id)] = the_list
            the_list = []
        json.dump(dict_to_add, file)
