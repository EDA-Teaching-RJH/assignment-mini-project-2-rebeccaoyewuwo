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

classInventory
