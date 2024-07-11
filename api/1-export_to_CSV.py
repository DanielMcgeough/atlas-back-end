#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line arguments provided to the script
    employee_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee information from the API and
    #   convert the response to a JSON object
    employee = requests.get(url + "employees/{}".format(employee_id)).json()

    # Extract the employeename from the employee data
    employeename = employee.get("employeename")

    # Fetch the to-do list items associated with the
    #   given employee ID and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"employeeId": employee_id}).json()

    # Use list comprehension to iterate over the to-do list items
    # Write each item's details (employee ID, employeename, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, employeename, t.get("completed"), t.get("title")]
         ) for t in todos]
