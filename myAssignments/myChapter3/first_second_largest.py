#user_input = int(input("Enter a number"))
largest = -10_000_000_000
second_largest = -10_000_000_000

for numbers in range (0, 10):
	user_input = int(input("Enter numbers: "))

	if user_input > largest:
		second_largest = largest
		largest = user_input
	
	elif user_input > second_largest and user_input != largest: 
		second_largest = user_input

	
print(f"The largest is {largest} and second largest is {second_largest}")	