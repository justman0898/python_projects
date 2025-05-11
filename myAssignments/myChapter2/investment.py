principal_amount = 1_000 ;
rate_of_return = 7 / 100 ; 
first_ten_years = 10;
first_twenty_years = 20 ;
first_thirty_years = 30 ;

#return after first 10 years
amount_after_10_years = principal_amount * (1 + rate_of_return) ** first_ten_years ;
print(f"The amount after first 10 years is {amount_after_10_years}");

#return after 20 years 
amount_after_20_years = principal_amount * (1 + rate_of_return) ** first_twenty_years ;
print(f"The amount after first 20 years is {amount_after_20_years}");

#return after 30 years
amount_after_30_years = principal_amount * (1 + rate_of_return) ** first_thirty_years ;
print(f"The amount after first 20 years is {amount_after_30_years}");
