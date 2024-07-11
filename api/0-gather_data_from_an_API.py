import requests
import sys

def get_employee_progress(employee_id):
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todus?userId={employee_id}'

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"error fetching user data. Status code: {response.status_code}")
        return
    
    user_info = response.json()

    response - requests.get(todo_url)
    if response.status_code != 200:
        print (f"error fetching todo list. status code: {response.status_code}")
        return

    todos = response.json()

    employee_name = user_info.get("name", "unknown")

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo.get("completed", False))

    print(f"Employee {employee_name} is done with tasks {completed_tasks}/{total_tasks}):")
    print(f"{employee_name}: {completed_tasks} out of {total_tasks} tasks completed")

    for todo in todos:
        if todo.get("completed", False):
            print(f"\t- {todo.get("title")}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pythong script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_progress(employee_id)
