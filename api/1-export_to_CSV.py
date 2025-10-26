#!/usr/bin/python3
"""This module exports an employee's ToDo list progress to a CSV file."""

import csv
import requests

import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])

    # Fetch employee info
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()
    username = user.get("username")

    # Fetch employee todos
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}").json()

    # Write to CSV
    filename = f"{emp_id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    emp_id,
                    username,
                    task.get("completed"),
                    task.get("title"),
                ]
            )
