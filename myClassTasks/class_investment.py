investment_amount = int(input("Enter investment amount:"))
number_of_years = int(input("Enter number of years:"))
interest_rate = int(input("Enter interest rate: ")) / 100
roi = 0

for years in range (1, number_of_years + 1):
	roi_temp = investment_amount * interest_rate
	roi = roi_temp + investment_amount	
	print(f"The return for year {years} is ${roi:,.2f}")
	investment_amount = roi