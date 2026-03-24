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
    def receipt(self):
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
            if not size:
                size = input("What size would you like? (small, medium, grande)").lower()
            if not re.match(r"^(small|medium|grande)$", size):
                print("Sorry lovely we only have small, medium and grande sizes.")
                return
        order = Order(item, size, qty)
        order.make()
        order.receipt()
        self.inventory.update_stock(item, qty)
        self.daily_sales.append(order)
    def find_item(self, item_name)
        pattern = re.compile(item_name.strip(), re.IGNORECASE)
        for item in self.menu:
            if pattern.search(item.name):
                return item
        return None
    def daily_report(self):
        print ("Showing daily report...")
        total = sum(order.item.price * order.qty for order in self.daily_sales)
        print(f"Total sales: £{total:2f}")

    def show_inventory(self):
        print("\nCurrent Inventory:")
        print("-" * 30)
        for ingredient, amount in self.inventory.stock.items():
            print(f"{ingredient}: {amount}")
        print("-" * 30) 

class Drink(MenuItem):
    def __init__(self, name, price, ingredients, steps, sizes):
        super().__init__(name, price, "drink", ingredients, steps, sizes)

class Food(MenuItem):
    def __init__(self, name, price, ingredients, steps):
        super().__init__(name, price, "food", ingredients, steps, sizes=[])

menu = [
    MenuItem(
        name = "Latte",
        price = 3.75,
        item_type = "drink",
        ingredients = {"Coffee Beans": 3, "Oat Milk": 2, "Cups": 1},
        steps = [
            "Grinding Coffee Beans...done!",
            "Preparing Coffee shot...done!",
            "Steaming Oat Milk...done!",
            "Pouring the Oat Milk & Coffee Shot into the cup...done!",
            "Enjoy your drink!"
        ],
        sizes = ["small", "medium", "grande"]
    ),
    MenuItem(
        name = "Mocha",
        price = 4.30,
        item_type = "drink",
        ingredients = {"Coffee Beans": 3, "Chocolate Syrup": 3, "Oat Milk": 2, "Cups": 1},
        steps = [
            "Pouring 3 tablespoons of chocolate syrup into the cup...done",
            "Grinding Coffee Beans...done!",
            "Preparing Coffee shot...done!",
            "Steaming Oat Milk...done!",
            "Pouring the Oat Milk & Coffee Shot into the cup...done!",
            "Enjoy your drink!"
        ],
        sizes = ["small", "medium", "grande"]
    ),
        MenuItem(
        name = "Matcha",
        price = 4.30,
        item_type = "drink"
        ingredients = {"Matcha Powder": 3, "Oat Milk": 2, "Cups": 1},
        steps = [
            "Pouring 1 heaping teaspoon of the matcha powder into the steaming cup...done",
            "Pouring Oat Milk into the steaming jug...done",
            "Steaming both the milk and powder together...done",
            "Pouring the mixture into a cup...done",
            "Enjoy your drink!"
        ],
        sizes = ["small", "medium", "grande"]
    ),
        MenuItem(
        name = "Hot Chocolate",
        price = 4.00,
        item_type = "drink",
        ingredients = {"Chocolate Syrup": 3, "Oat Milk": 2, "Cups": 1},
        steps = [
            "Pouring 4 tablespoons into the steaming jug...done",
            "Pouring Oat Milk into the steaming jug..done",
            "Steaming the mixture...done",
            "Pouring the mixture into a cup...done",
            "Enjoy your drink!"
        ],
        sizes = ["small", "medium", "grande"]
    ),
        MenuItem(
        name = "Ham & Cheese Sando",
        price = 5.50,
        item_type = "food",
        ingredients = {"Ham": 2, "Cheese": 2, "Bread": 2, "Mayo": 1, "Paper Food Bag": 1},
        steps = [
            "Toasting the bread...done",
            "Squirting the mayo onto the two toasted silces of bread...done",
            "Adding the ham and cheese...done",
            "Toasting the sando with the ham & cheese...done",
            "Putting the sando into the paper food bag...done",
            "Enjoy the sando!"
        ],
        sizes = []
    ),
        MenuItem(
        name = "Vegan BLT",
        price = 5.75,
        item_type = "food",
        ingredients = {"Vegan Ham": 2, "Tomato": 2, "Lettuce": 2, "Bread": 2, "Mayo": 2, "Paper Food Bag": 1},
        steps = [
            "Toasting the bread...done",
            "Squirting the mayo onto the two toasted silces of bread...done",
            "Adding the vegan ham, tomato and lettuce...done",
            "Cutting the BLT in half...done",
            "Putting the sandwich into the paper food bag...done",
            "Enjoy your sandwich!"
        ],
        sizes = []
    ),
        MenuItem(
        name = "Tuna & Egg Sando",
        price = 5.40,
        item_type = "food",
        ingredients = {"Tuna": 2, "Egg": 2, "Bread": 2, "Mayo": 2, "Paper Food Bag": 1},
        steps = [
            "Toasting the bread...done",
            "Squirting the mayo onto the two toasted bread slices...done",
            "Adding the tuna and egg on the two slices...done",
            "Putting the sando into the paper food bag...done",
            "Enjoy your sando!"
        ],
        sizes = []
    ),
        MenuItem(
        name = "Avocado & Egg Sando",
        price = 6.80
        item_type = "food"
        ingredients = {"Avocado": 2, "Egg": 2, "Bread": 2, "Mayo": 2, "Tomato": 1, "Lettuce": 1, "Paper Food Bag": 1},
        steps = [
            "Toasting the bread...done",
            "Squirting the mayo onto the two slices of bread...done",
            "Mashing the avocado and spreading it onto the bread...done",
            "Adding the egg, tomato and lettuce into the sando...done",
            "Putting the sandwich into the paper food bag...done",
            "Enjoy your sando!"
        ],
        sizes = []
    ),
]

def main():
    Inventory = inventory(inventory_stock)
    cafe_instance = cafe(menu, inventory)
    print("Welcome to The Oat & Bean Cafe!")
    cafe_instance.show_menu()

    While True: #loops for multiple customers
        While True:
            cafe_instance.take_order()
            again = input ("Is there anything else you would love? (yes/no)")
            if again.lower() !="yes":
                cafe_instance.current_personality = None
                break
        another_customer = input("\nNew customer coming in? (yes/no)")
        if another_customer.lower() != "yes":
            break
    cafe_instance.daily_report()

    show_inventory = input ("\nWould you like to see the inventory? (yes/no)")
    if show_inventory.lower() == "yes":
        cafe_instance.show_inventory()

    print("Thank you so much lovely!")

