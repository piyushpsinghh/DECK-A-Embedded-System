import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	try:
		length = int(input("Enter password length: "))
	except ValueError as val:
		print("Enter a Valid Input")
		length = int(input("Enter password length: "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))
	input("Press Enter to Continue")
# generate_random_password()
# print(type(a))
#piyush
