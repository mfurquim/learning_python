#!/bin/env python
import json


my_json = json.loads(
    """{
        "sensors": [
            {"date": "1/1/1", "code": 1},
            {"date": "2/2/2", "code": 2},
            {"date": "3/3/3", "code": 3}
        ]
        }
"""
)

print(my_json)

my_list = my_json["sensors"]

print(my_list)


allowed = [code["code"] for code in my_list]

codes = [1, 3, 5]

for code in codes:
    print(code)

    if code not in allowed:
        print("not in")
    else:
        print("yes in")
