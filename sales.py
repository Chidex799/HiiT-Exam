import json
import random
from product import create_product

class Sales:
    def __init__(self):
        self.sales_date = input("Enter sales date: ")
        self.product_tile = input("Enter product title: ")
        self.quantity_sold = input("Enter quantity sold: ")
        self.total_price = input("Enter total price: ")

        sales = {
            "sales_date": self.sales_date,
            "product_tile": self.product_tile,
            "quantity_sold": self.quantity_sold,
            "total_price": self.total_price
        }

        json_objects = json.dumps(sales, indent=4)
        with open("sales.json", "w+") as json_file:
            json_file.write(json_objects)
