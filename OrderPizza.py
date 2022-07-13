# OrderPizza.py
# yfirstProjects

# Created by Dmytro Lytvynenko 7/10/2022


import os
import time
available_pizzas = ["margarita", "hawaii", "supermeat", "4cheese", "vegetarian"]
available_toppings = ["mushrooms", "cheese", "pepperoni", "olives", "bacon"]
pizza_prices = {"margarita": 5.99, "hawaii": 6.38, "supermeat": 7.19, "4cheese": 7.25, "vegetarian": 5.89}
toppings_prices = {"mushrooms": 1.59, "cheese": 1.15, "pepperoni": 1.01, "olives": 1.14, "bacon": 1.29}

#Created ShowMenu function to show our available pizzas and toppings for pizza

def ShowMenu():
    os.system('cls')
    print("Available Pizzas:")
    print(*available_pizzas, sep=', ')
    time.sleep(2.5)
    print("\n")
    print("Available toppings:")
    print(*available_toppings, sep=', ')
    time.sleep(2.5)
    
#TakingUserOrder function call ShowMenu function to customer with our menu and TakingUserOrder asking our customer to make order.

def TakingUserOrder():
    os.system('cls')
    print("Hello, Welcome to Python Pizza House!\n")
    time.sleep(1)
    ordering = True
    while ordering:
        os.system('cls')
        ShowMenu()
        ask_order = (input("\nEnter what pizza do you want to order: "))
        if ask_order.lower() not in available_pizzas:
            print(f"Sorry, we don't have {ask_order}")
            os.system('pause')
            continue
        time.sleep(0.5)
        
        #In this section we asking our customer does he/she want to add some available topping
        #If not we finish generate our pizza and print order without topping
        
        ask_topping1 = (input(f"Enter a topping , if you don't want to add some toppings enter 'no':"))
        if ask_topping1.lower() == "no":
            print(f"Your order is {ask_order}")
        if ask_topping1.lower() not in available_toppings:
            print(f"Sorry, we don't have {ask_topping1}\n")
            os.system('pause')
            continue
        print(f"Adding {ask_topping1.title()} to your order...")
        time.sleep(1.5)
        print(f"Your order is {ask_order.title()} with topping {ask_topping1.title()}")
        return ask_order, ask_topping1
    
#Here we use OOP and  call Order class 

class Order:
    def __init__(self):
        ask_order, ask_topping1 = TakingUserOrder()
        self.type = ask_order
        self.topping1 = ask_topping1
        self.PizzaPrice = pizza_prices[ask_order]
        self.Topping1Price = toppings_prices[ask_topping1]
        self.Total = self.PizzaPrice + self.Topping1Price

# In this part of code we asking about a new order 
        
users_input = True
orders = []
orderchoice = input("Welcome! Would you like to order ? (Yes or No): ")
if orderchoice.lower() == 'n':
    print("Have a nice day!")
else:
    while users_input:
        neworder = Order()
        orders.append(neworder)
        newchoice = input("Would you like to order again? (y/n): ")
        if newchoice.lower() == 'n':
            break

total = 0
for order in orders:
    total += order.Total

print(f"Total of your order is: {total}", "$")
