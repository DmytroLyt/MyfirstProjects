class Math:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def multipliction(self, x, y):
        multiply = x * y
        print(multiply)

    def division(self, x, y):
        divide = x / y
        print(divide)

    def addition(self, x, y):
        add = x + y
        print(add)

    def substraction(self, x, y):
        substract = x - y
        print(substract)

user_num1 = float(input("Enter your first number: "))
user_num2 = float(input("Enter your second number: "))
user_operator = input("Enter your operator: ")

calc = Math(user_num1, user_num2, user_operator)
if user_operator == "*":
    calc.multipliction(calc.num1, calc.num2)
elif user_operator == "/":
    calc.division(calc.num1, calc.num2)
elif user_operator == "+":
    calc.addition(calc.num1, calc.num2)
elif user_operator == "-":
    calc.substraction(calc.num1, calc.num2)
else:
    print("Invalid input")
