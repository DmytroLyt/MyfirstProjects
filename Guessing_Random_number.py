import random

num = random.randint(0,50)

attempt = 10
while attempt!=0:
	user_input=int(input('Enter number between 1 and 50: '))
	
	if user_input>num:
		print (f'Try again, your number is higher! {attempt-1} attempt left')
	elif user_input<num:
		print (f'Try again, your number is lower! {attempt-1} attempt left')
	elif user_input ==num:
		print('You won!I wished number '+str(num) )
		break
	attempt-=1
else:
	print ('Game is over!')
	