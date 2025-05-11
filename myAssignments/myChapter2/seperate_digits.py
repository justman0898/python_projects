five_digit_integer = int(input("Enter a five digit integer: "))

first_digit = five_digit_integer // 10000 ;
second_digit = (five_digit_integer // 1000) % 10 ;
third_digit = (five_digit_integer // 100) % 10 ;
fourth_digit = (five_digit_integer // 10) % 10 ;
fifth_digit = five_digit_integer % 10 ;

print(f"{first_digit}\t{second_digit}\t{third_digit}\t{fourth_digit}\t{fifth_digit}");					


	