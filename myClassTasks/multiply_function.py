def multiply_two_integers(number1, number2): 
	product = 0
	sum = 0
	if number2 < 0: 
		number2 = abs(number2)	
		number2_integer = int(number2)
		for numbers in range (0,number2_integer):
			product = product + number1

		#fractiional part
		integer_part = int(number2)
		frac_part = round(number2 - integer_part, 1)
		loop_control = int(frac_part * 10) 
		number1_tenth = number1 /10
		for _ in range (loop_control):
			sum = sum + number1_tenth
		product = product + sum
		
		return -(product)
	else:
		"""
		for numbers in range (0,number2):
			product = product + number1
		"""
		return product
	
result = multiply_two_integers(8, -891.9)
print(result)

	