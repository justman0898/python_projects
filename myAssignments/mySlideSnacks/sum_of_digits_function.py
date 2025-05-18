
def sum_of_digits(number):
	if number >= 1 and number <= 10000:
		sum_total_of_digit = 0
		while number != 0:
			digit = number % 10
			sum_total_of_digit = sum_total_of_digit + digit
			number = number // 10
		return sum_total_of_digit
	else: 
		return f"Out of range"

number = 1451888
sum = sum_of_digits(number)
print(sum)