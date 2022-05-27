#!/usr/bin/python3
"""Script to export all employee data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    uid = sys.argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(uid))
    name = usr.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    file = uid + '.csv'
    with open(file, mode='w') as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(uid):
                write.writerow([uid, name, str(task.get('completed')),
                                task.get('title')])
