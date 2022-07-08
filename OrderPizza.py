toppings = ("mushrooms", "cheese", "pepperoni", "olives", "bacon")
ask_order = (input("Welcome to our Python Pizza! Do you want to make order? Print yes or no: "))
pizza = ""
if ask_order.lower() == 'yes':
    print("All right. Let`s customize your pizza!")
    ask_topping1 = (input(f"You can choose two toppings: {toppings}"))
    if ask_topping1.lower() == "mushrooms":
        pizza += ask_topping1
        print(f"Adding {ask_topping1} to your pizza!")
    if ask_topping1.lower() == "cheese":
        pizza += ask_topping1
        print(f"Adding {ask_topping1} to your pizza!")
    if ask_topping1.lower() == "pepperoni":
        pizza += ask_topping1
        print(f"Adding {ask_topping1} to your pizza!")
    if ask_topping1.lower() == "olives":
        pizza += ask_topping1
        print(f"Adding {ask_topping1} to your pizza!")
    if ask_topping1.lower() == "bacon":
        pizza += ask_topping1
        print(f"Adding {ask_topping1} to your pizza!")
    ask_customer = (input("Do you want to add more toppings? Yes or no?: "))
    if ask_customer.lower() == "yes":
        ask_topping2 = (input(f"Cool. Let`s choose some more toppings: {toppings}"))
        if ask_topping2.lower() == "mushrooms":
            pizza += ask_topping2
            print(f"Adding {ask_topping2} to your pizza!")
        if ask_topping2.lower() == "cheese":
            pizza += ask_topping2
            print(f"Adding {ask_topping2} to your pizza!")
        if ask_topping2.lower() == "pepperoni":
            pizza += ask_topping2
            print(f"Adding {ask_topping2} to your pizza!")
        if ask_topping2.lower() == "olives":
            pizza += ask_topping2
            print(f"Adding {ask_topping2} to your pizza!")
        if ask_topping2.lower() == "bacon":
            pizza += ask_topping2
            print(f"Adding {ask_topping2} to your pizza!")
        print(f"Okay. Your order standard pizza with {pizza} and {pizza}.")
    else:
        print(f"Okay. Your order standard pizza with {pizza}.")
else:
    print("Have a nice day!")