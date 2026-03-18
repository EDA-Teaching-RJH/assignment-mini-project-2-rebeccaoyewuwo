from datetime import datetime
import random
import re

def clean_input(text):
    return re.sub(r"\s+", " ", text).strip()
#removing extra spaces, tabs and double spaces

class MenuItem:
    def __init__ (self, name, price, item_type, ingredients, steps, sizes):
        self.name = name
        self.price = price
        self.type = item_type
        self.ingredients = ingredients 
        self.steps = steps
        self.sizes = sizes

class Inventory:
    def __init__(self, stock):
        self.stock = stock

    def has_ingredients(self, item):
        for ingredient, amount in item.ingredients.items():
            if self.stock.get(ingredient, 0) < amount:
                return False, ingredient
        return True, None
    def update_stock(self, item, qty=1):
        for ingredient, amount in item.ingredients.items():
            self.stock[ingredient] -= amount * qty    