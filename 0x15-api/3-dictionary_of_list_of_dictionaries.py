#!/usr/bin/python3
"""
Gets employee info from API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users'.format(url)
    req = requests.get(user)
    data = req.json()
    user_data = {}

    # create dictionary with all user data
    for user in data:
        userid = user.get('id')
        username = user.get('username')
        todos = '{}todos?userId={}'.format(url, userid)
        req = requests.get(todos)
        data1 = req.json()
        tasks = []
        for task in data1:
            new_dict = {"username": username,
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            tasks.append(new_dict)

        user_data[str(userid)] = tasks

    # create json file
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as f:
        json.dump(user_data, f)
