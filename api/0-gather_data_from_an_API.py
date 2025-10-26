#!/usr/bin/python3
"""Gather and display an employee's ToDo progress from a REST API.

This small script fetches user information and the user's todo list from
the JSONPlaceholder test API (https://jsonplaceholder.typicode.com/) and
prints how many tasks are completed along with the titles of the completed
tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Example:
    python3 0-gather_data_from_an_API.py 2

Outputs (printed to stdout):
    Employee <Name> is done with tasks(<done>/<total>):
        <completed task title 1>
        <completed task title 2>

Notes:
    - This script depends on the `requests` library. Install with:
        pip install requests
    - The script is intentionally small and intended for educational/demo use.
    - Minimal argument validation is provided; network errors are not caught
      here to keep the example concise.
"""

import sys
from typing import List, Dict

import requests


def _print_usage_and_exit() -> None:
    """Print a short usage message and exit with a non-zero status.

    Kept as a separate helper so the script remains readable and the
    usage text is easy to update if needed.
    """
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)


if __name__ == "__main__":
    # Basic argument validation: ensure an employee id was provided.
    if len(sys.argv) < 2:
        _print_usage_and_exit()

    # Convert the provided argument to an integer. This will raise a ValueError
    # and terminate the script if the value is not a valid integer. That behavior
    # is acceptable for this small demo script.
    emp_id = int(sys.argv[1])

    # Fetch employee info from the test API. The `.json()` call returns a dict
    # containing user fields such as 'name', 'email', etc.
    user: Dict = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    ).json()

    # Fetch todos for the given user. The API returns a list of task objects.
    todos: List[Dict] = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    ).json()

    # Count total tasks and filter those marked as completed.
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print a human-readable summary: the employee name and completed/total
    # counts, followed by the titles of completed tasks.
    print(
        f"Employee {user.get('name')} is done with tasks({len(done_tasks)}/{total_tasks}):"
    )
    for task in done_tasks:
        # Each task is a dict; 'title' stores the task description.
        print(f"\t {task.get('title')}")
