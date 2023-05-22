#!/usr/bin/python3
"""
Gets employee info from API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, argv[1])
    req = requests.get(user)
    data = req.json()
    userid = argv[1]
    username = data.get('username')

    todos = '{}todos?userId={}'.format(url, argv[1])
    req = requests.get(todos)
    data = req.json()
    tasks = []

    for task in data:
        new_dict = {"task": task.get('title'), "completed": task.get('completed'),
                    "username": username}
        tasks.append(new_dict)

    user_data = {str(userid): tasks}
    file_name = '{}.json'.format(userid)
    with open(file_name, 'w') as f:
        json.dump(user_data, f)
