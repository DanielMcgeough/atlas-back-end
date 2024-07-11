#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee in CSV form.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    """Get the employee ID from the command_lie arguemnts
    provided to the script
    """
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    """Fetch employee information from the API
    and conver the response to a JSON object"""
    employee = requests.get(url + "employees/{}".format(employee_id)).json()

    EmployeeName = employee.get("EmployeeName")

    todos = requests.get(
        url + "todos",
        params={"employeeid": employee_id}
    ).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, EmployeeName, t.get("completed"), t.get("title")]
        ) for t in todos]
