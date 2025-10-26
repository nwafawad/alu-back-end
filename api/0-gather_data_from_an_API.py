#!/usr/bin/python3
import requests
import sys

# Python script that fetches and displays an employee’s ToDo list progress from a REST API

if __name__ == "__main__":
    emp_id = int(sys.argv[1])

    # Fetch employee info
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()

    # Fetch employee todos
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}").json()

    # Process tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print results
    print(f"Employee {user.get('name')} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
