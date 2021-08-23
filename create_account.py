import json
import random


def create_staff_account():
    print("\n Create your account \n")
    id = random.randrange(1, 10)
    email = input("enter your email: ")
    password = input("enter your password: ")

    staff = {
        "id": id,
        "email": email,
        "password": password
    }

    json_object = json.dumps(staff, indent=4, sort_keys=True)

    with open("staffs.json", "a+") as json_file:
        json_file.write(json_object)

    print("account created sucessfully")
