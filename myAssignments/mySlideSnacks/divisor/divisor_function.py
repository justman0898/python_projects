def get_multiples(*numbers, divisor=2):
	count = 0
	are_multiples = []	
	if  isinstance(divisor, (int, float)) == False or divisor == 0 :
		return f"Error divisor cannot be zero or must be a number"

	for each in numbers:
		if isinstance(each, (int, float)) == False:
			return f"Not a number"

	for multiples in numbers:
		if multiples % divisor == 0:
			count += 1
			are_multiples.append(multiples)
	if count > 0:
		return tuple(are_multiples)
	else:
		return f"No Multiple Found"
			




			