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

# inventory stock for the cafe
inventory_stock = {
    "Coffee Beans": 100,
    "Oat Milk": 100,
    "Cups": 100,
    "Paper Food Bag": 100,
    "Bread": 75,
    "Chocolate Syrup": 50,
    "Mayo": 50,
    "Matcha Powder": 45,
    "Chai Powder": 45,
    "Cinnamon Powder": 40,
    "Tomato": 40,
    "Lettuce": 40,
    "Egg": 40,
    "Ham": 20,
    "Cheese": 20,
    "Vegan Ham": 20,
    "Tuna": 20,
    "Avocado": 20,
}