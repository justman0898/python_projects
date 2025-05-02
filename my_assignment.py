

no_of_years = int(input("Enter the duration in years: "));

principal = float(input("Enter the principal amount: "));

rate = float(input("Enter the annual interst rate: "));

monthly_rate = (rate / 100) /12 # Conversion mechanism

number_of_months = no_of_years * 12 # Conversion mechanism

inner_bracket = (1 + monthly_rate);

exponent = ( monthly_rate * (inner_bracket ** number_of_months) ) * principal;

denominator = (inner_bracket ** number_of_months ) - 1 ;

monthly_payment = exponent / denominator; 

print("Your monthly payment is: $ ", monthly_payment);

	
	