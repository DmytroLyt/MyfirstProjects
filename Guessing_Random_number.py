import random

num = random.randint(0, 30)

attempt = 5
while attempt != 0:
    while True:
        try:
            user_input = int(input('Enter number between 0 and 30: '))
        except ValueError:
            print("Invalid value, please enter a digits")
            continue
        else:
            break
    if user_input not in range(0, 31):
        print("Your number is out of range. Please try again")
        continue
    if user_input > num:
        print(f'Try again, your number is higher! {attempt - 1} attempt left')
    elif user_input < num:
        print(f'Try again, your number is lower! {attempt - 1} attempt left')
    elif user_input == num:
        print('You won!I wished number ' + str(num))
        break
    attempt -= 1
else:
    print('Game is over!')
