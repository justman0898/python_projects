MY_PASSWORD = input("Enter a valid password: ");

if len(MY_PASSWORD) < 8:
	print("Very Weak")
elif len(MY_PASSWORD) == 8:
	print("Weak")
elif len(MY_PASSWORD) >= 8 and len(MY_PASSWORD) <= 16:
	print("Strong")
elif len(MY_PASSWORD):
	print("Very Strong")
else:
	print("Invalid Password")