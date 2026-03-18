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
        match = pattern.match(text)
        if not match:
            return None, None, None
        
        quantity = match.group(1)
        size = match.group(2)
        item_name = match.group(3)

        return int(quantity) if quantity else 1, size, item_name.strip()
    def search_menu(self, pattern):
        regex = re.compile(pattern, re.IGNORECASE)
        return [item for item in self.menu if regex.search(item.name)]
    
    def __init__(self, menu, inventory):
        self.menu = menu
        self.inventory = inventory
        self.daily_sales = []
        self.personalities = ["friendly", "grumpy", "shy", "chatty"]
        self.current_personality = None
        
    def show_menu(self):
        print("Here's the menu")
        for item in self.menu:
            print(f"{item.name} - £{item.price} ({item.type})")
    
    def take_order(self):
        if self.current_personality is None:
            self.current_personality = random.choice(self.personalities)
        print(f"\nA {self.current_personality} customer approaches the counter...")

        choice = input("What would you like to order lovely?")
        qty, size, item_text = self.parse_order_input(choice)
        item = self.find__item(item_text)
        if not item:
            print("Sorry lovely, that's not on the menu! Please choose something on the menu.")
            return
        ok, missing_ingredient = self.inventory.has_ingredients(item)
        if not ok:
            print(f"Sorry we are out of {missing_ingredient}. Please choose something else.")
            return
        size = None
        if item.type == "drink":
            #if the customer chooses the wrong size