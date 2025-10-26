#!/usr/bin/python3
"""
Module 2-export_to_JSON
-----------------------
Exports all tasks owned by a given employee to a JSON file.

Usage:
    ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


def fetch_user(emp_id):
    """
    Fetch user information from the API.

    Args:
        emp_id (int): The employee ID.

    Returns:
        dict: JSON object containing user data.
    """
    return requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    ).json()


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
    emp_id = int(sys.argv[1])
    user = fetch_user(emp_id)
    todos = fetch_todos(emp_id)

    # Build JSON structure
    data = {str(emp_id): []}
    for task in todos:
        data[str(emp_id)].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Write to file
    filename = f"{emp_id}.json"
    with open(filename, "w") as file:
        json.dump(data, file)
