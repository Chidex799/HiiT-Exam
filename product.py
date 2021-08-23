import random
import json
from os import remove


def create_product():
    id = random.randrange(1, 10)
    tile = input("enter title: ")
    quantity = input("enter quantity: ")
    price = input("enter price: ")

    products = {
        "product_id": id,
        "product_title": tile,
        "product_quantity": quantity,
        "product_price": price
    }

    with open("products.json", "a+") as json_file:
        json.dump(products, json_file, indent=1)

def read_products():
    with open("products.json") as json_file:
        products = json.loads(str(json_file.read()))
        print("title", products["product_title"])
        print("quantity", products["product_quantity"])
        print("price", products["product_price"])

def update_products():
    with open("products.json") as json_file:
        products = json.loads(str(json_file.read()))
        print("current product ", products)

        new_title = input("enter new tilte: ")
        new_quantity = input("enter new quantity: ")
        new_price = input("enter new price: ")

        data = {
            "product_id": random.randrange(1,100),
            "product_title": new_title,
            "product_quantity": new_quantity,
            "product_price": new_price
        }

        with open("products.json", "w+") as json_file_2:
            json.dump(data, json_file_2, indent=1)
            print("\n Update success")

def delete_products():
    remove("products.json")