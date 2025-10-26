#!/usr/bin/python3
"""
Python script that fetches and displays an employee's ToDo list
progress from a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])

    # Fetch employee info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    ).json()

    # Fetch employee todos
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    ).json()

    # Process tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print results
    name = user.get("name")
    done_count = len(done_tasks)

    print(
        f"Employee {name} is done with tasks({done_count}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task.get('title')}")
