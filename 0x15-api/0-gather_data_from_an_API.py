#!/usr/bin/python3
"""
Gets employee info from API
"""
import requests
from sys import argv


if __name__ == "__main__":

    tasks_done = 0
    total_tasks = 0
    tasks = []

    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, argv[1])
    req = requests.get(user)
    data = req.json()

    e_name = data.get('name')
    todos = '{}todos?userId={}'.format(url, argv[1])
    req = requests.get(todos)
    data = req.json()

    for task in data:
        total_tasks += 1
        if task.get('completed') is True:
            tasks_done += 1
            tasks.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
                                                   e_name,
                                                   tasks_done,
                                                   total_tasks
                                                   ))
    for task in tasks:
        print("\t " + task)
