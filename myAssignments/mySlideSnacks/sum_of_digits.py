number = int(input("Enter a number between 1 to 10,000: "))
if number >= 1 and number <= 10000:
	sum_total_of_digit = 0
	while number != 0:
		digit = number % 10
		sum_total_of_digit = sum_total_of_digit + digit
		number = number // 10
	print(sum_total_of_digit)
else: 
	print(f"Out of range")
