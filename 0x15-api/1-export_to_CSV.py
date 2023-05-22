#!/usr/bin/python3
"""
Gets employee info from API
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = argv[1]
    user = '{}users/{}'.format(url, argv[1])
    req = requests.get(user)
    data = req.json()
    username = data.get('username')

    todos = '{}todos?userId={}'.format(url, argv[1])
    req = requests.get(todos)
    data = req.json()
    tasks = []

    for task in data:
        tasks.append([userid,
                      username,
                      task.get('completed'),
                      task.get('title')])

    filename = '{}.csv'.format(userid)

    with open(filename, 'w') as csvfile:
        e_data = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for task in tasks:
            e_data.writerow(task)
