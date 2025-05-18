total = 0
count = 0
average = 0


gallon = float(input("Enter amount of gallon used or -1 to end: "))
miles = float(input("Enter miles driven: "))

while gallon != -1 or miles != -1:
	miles_per_gallon = miles / gallon
	total = total + miles_per_gallon
	count += 1
	print("The miles per gallon for this tank was %.2f" %total)
	gallon = float(input("Enter gallons used(-1 to end): "))
	if gallon == -1:
		break 
		
	miles = float(input("Enter miles driven: "))
	if miles == -1:
		break 
	
	

if total > 0 :
	average = total / count
	print(f"The average is {average:,.2f}")

	
	
		