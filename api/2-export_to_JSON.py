#!/usr/bin/python3
"""task-2"""
import requests
import json
from sys import argv

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
    the_list = []
    with open("{}.json".format(user_id), "w") as file:
        for i in r_todos:
            if i["userId"] == user_id:
                the_list.append({
                    "task": i['title'],
                    "completed": i["completed"],
                    "username": username_task
                })
        json.dump({str(user_id): the_list}, file)
