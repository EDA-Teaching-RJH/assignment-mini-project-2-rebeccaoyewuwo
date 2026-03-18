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

class Order:
    def __init__(self, item, size=None, qty=1):
        self.item = item
        self.size = size
        self.qty = qty
    def make(self):
        print(f"Prepping your {self.qty} x {self.item.name}...")
        for step in self.item.steps:
            print(step)
    def receipt(self)
        #Here I am going to write the code that describes how i have made the text reciept
        timestamp = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        filename = f"receipt_{timestamp}.txt"

        try:
            with open(filename, "w") as file:
                file.write("The Oat & Bean Cafe receipt\n")
                file.write("---------------------------\n")
                file.write(f"item : {self.qty} x {self.item.name}\n")
                if self.size:
                    file.write(f"size: {self.size}\n")
                file.write(f"price: £{self.item.price * self.qty: .2f}\n")
                file.write("---------------------------\n")
                file.write("Thank you so much for purchasing at The Oat & Bean!")

        print(f"\n Receipt has been printed, Thank you!")

class Cafe:
    def parse_order_input(text):
        """
        Extracts quantity, size, and item name from mess customer input.
        Examples :
        - '2x large mocha'
        - 'large latte'
        - 'matcha grande please'
        - '3 medium chai latte'
        -'latte'
        """

        text = clean_input(text.lower())

        pattern = re.compile(
            r"^(?:(\d+)\s*x?\s*)?"              #qty like 2x
            r"(?:(small|medium|grande)\s+)?"    #size
            r"(.+?)$"                           #item name
        )
        