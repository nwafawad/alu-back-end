#!/usr/bin/python3
"""
Module 3-dictionary_of_list_of_dictionaries
-------------------------------------------
Exports all employees' tasks to a single JSON file.

Output file:
    todo_all_employees.json
"""

import json
import requests


def fetch_users():
    """
    Fetch all users from the API.

    Returns:
        list: List of user dictionaries.
    """
    return requests.get("https://jsonplaceholder.typicode.com/users").json()


def fetch_todos(emp_id):
    """
    Fetch all TODO tasks for a given employee.

    Args:
        emp_id (int): The employee ID.

    Returns:
        list: List of task dictionaries.
    """
    return requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    ).json()


if __name__ == "__main__":
    users = fetch_users()
    data = {}

    for user in users:
        emp_id = user.get("id")
        username = user.get("username")
        todos = fetch_todos(emp_id)

        data[str(emp_id)] = []
        for task in todos:
            data[str(emp_id)].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # Write to file
    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)
