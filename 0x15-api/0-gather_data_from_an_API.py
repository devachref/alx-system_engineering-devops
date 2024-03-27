#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()

    employee_name = user_data.get('name')

    todo_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

