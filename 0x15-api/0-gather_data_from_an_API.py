#!/usr/bin/python3
"""
Gets employee info from API
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, argv[1])
    req = requests.get(user)
    data = req.json()

    e_name = data.get('name')
    todos = '{}todos?userId={}'.format(url, argv[1])
    req = requests.get(todos)
    data = req.json()
    tasks = []

    for task in data:
        if task.get('completed') is True:
            tasks.append(task)


    print('Employee {} is done with tasks({}/{}):'.format(
                                                   e_name,
                                                   len(tasks),
                                                   len(data)
                                                   ))
    for task in tasks:
        print("\t{}".format(task.get("title")))
