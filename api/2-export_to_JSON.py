#!/usr/bin/python3
"""
Exports the to do list info for a
employee determined by the employee id
and then exports the data to a JSON
file
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "http://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)), json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(url + "todos")

    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
