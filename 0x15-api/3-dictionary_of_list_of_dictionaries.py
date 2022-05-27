#!/usr/bin/python3
"""script to export all employees data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    usr = requests.get("https://jsonplaceholder.typicode.com/users")
    usr = usr.json()
    toDo = requests.get('https://jsonplaceholder.typicode.com/todos')
    toDo = toDo.json()
    todo_A = {}

    for user in usr:
        taskList = []
        for task in toDo:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todo_A[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_A, f)
