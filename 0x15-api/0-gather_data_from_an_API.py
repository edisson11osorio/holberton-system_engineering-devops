#!/usr/bin/python3
"""returns an employee ToDo list progress using a REST-API"""
import requests
import sys

if __name__ == "__main__":

    toDo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    user_n = user.get('name')
    user_id = user.get('id')
    tasks = []
    doneTasks = 0
    totalTasks = 0

    for stat in toDo:
        if user_id == stat.get('userId'):
            if stat.get('completed') is True:
                doneTasks = doneTasks + 1
                tasks.append(stat.get('title'))
            totalTasks = totalTasks + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_n, doneTasks, totalTasks))

    for data in tasks:
        print('\t', data)
