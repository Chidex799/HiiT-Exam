import random
import json


def login():
    print("\n......LOGIN.....\n")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open("staffs.json") as json_file:
        data = json.loads(str(json_file.read()))

        if email == data["email"] and password == data["password"]:
            print("Access granted")

        else:
            print("Invalid email or password")
            login()


