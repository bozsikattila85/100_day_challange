# 1.Print report
# 2.Check resources
# 3.Process coins
# 4.Check transaction successful
# 5.Make coffee


class CoffeeMachine:

    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "milk": 0,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }

    def __str__(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"

    def is_enough(self, ingredient_type, amount):
        return amount <= getattr(self, ingredient_type)

    def is_enough_for(self, recipe):
        return (self.is_enough("water", self.MENU[recipe]["ingredients"]["water"]) and
                self.is_enough("milk", self.MENU[recipe]["ingredients"]["milk"]) and
                self.is_enough("coffee", self.MENU[recipe]["ingredients"]["coffee"])
                )

    def get_recipe_price(self, recipe):
        return self.MENU[recipe]["cost"]

    def get_missing_resources(self, recipe):
        missing = ""
        if not self.is_enough("water", self.MENU[recipe]["ingredients"]["water"]):
            missing += "Sorry theres not enough water.\n"
        if not self.is_enough("milk", self.MENU[recipe]["ingredients"]["milk"]):
            missing += "Sorry theres not enough milk.\n"
        if not self.is_enough("coffee", self.MENU[recipe]["ingredients"]["coffee"]):
            missing += "Sorry theres not enough coffee.\n"
        return missing

    def sub_recources(self, recipe):
        self.water -= self.MENU[recipe]["ingredients"]["water"]
        self.milk -= self.MENU[recipe]["ingredients"]["milk"]
        self.coffee -= self.MENU[recipe]["ingredients"]["coffee"]

    def get_coins(self):
        print("Please insert coins.")
        quarters = int(input("quarters:"))
        dimes = int(input("dimes:"))
        nickles = int(input("nickles:"))
        pennies = int(input("pennies:"))
        return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    def order_processing(self, choice):
        if self.is_enough_for(choice):
            coins = self.get_coins()
            if coins >= self.get_recipe_price(choice):
                self.money += self.get_recipe_price(choice)
                coins -= self.get_recipe_price(choice)
                self.sub_recources(choice)
                print(f"Espresso is done, enjoy!\nHere is ${coins:.2f} dollars in change.")
            else:
                print(f"Sorry that's not enough money. Returning ${coins} dollars.")
        else:
            print(self.get_missing_resources(choice))

    def run(self):
        choice = ""
        while choice != "off":
            choice = input("What would you like? (espresso/latte/cappuccino):")
            if choice == "espresso":
                self.order_processing(choice)
            if choice == "latte":
                self.order_processing(choice)
            if choice == "cappuccino":
                self.order_processing(choice)
            if choice == "report":
                print(self.__str__())


a = CoffeeMachine()
a.run()