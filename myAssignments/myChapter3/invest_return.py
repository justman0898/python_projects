principal = 1_000
rate = 7 / 100
noOfYears = 0

for years in range (1,31):
	noOfYears = years	
	amount = principal * ((1 + rate)**noOfYears)

	print(f"Amount at the end of year {years} is: ${amount:,.2f}")
