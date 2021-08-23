from os import read
from create_account import create_staff_account
from login import login
from product import create_product, read_products, update_products, delete_products
from sales import Sales

print("******** Name: Chime Praise Chidi *************\n")

print("*********** Product Management System *********")

print("Welcome Boss")

name = input("please enter your name: ")

print("Good day " + name)


def options():
    print("press 1 to create an account: ")
    print("press 2 to login: ")
    response = input("Enter response: ")
    if response == "1":
        print("\nN.B: please endeavour to delete previous records on all json files before creating new ones \n")
        create_staff_account()
    elif response == "2":
        login()
    else:
        print("invalid response try again")
        options()


options()


def option2():
    print("************ welcome to sales section *************")
    print("press 3 to record sale")
    print("press 4 to exit")
    response = input("please enter your response: ")
    if response == "3":
        Sales()
    elif response == "4":
        print("exit")
    else:
        print("invalid response")
        option2()
option2()


def option3():
    print("****** welcome to the product section ***********")
    print("press 5 to create")
    print("press 6 to read")
    print("press 7 to update")
    print("press 8 to delete")
    print("press 9 to exit")
    response = input("Please enter your response: ")
    if response == "5":
        create_product()
    elif response == "6":
        read_products()
    elif response == "7":
        update_products()
    elif response == "8":
        delete_products()
    elif response == "9":
        print("exit")
    else:
        print("invalid response")
        option3()


option3()
