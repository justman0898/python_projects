number_1 = int(input("Enter the first number: "));
number_2 = int(input("Enter the first number: "));
number_3 = int(input("Enter the first number: "));

if number_1 > number_2 :
	temporary_holder = number_1
	number_1 = number_2
	number_2 = temporary_holder

if number_1 > number_3 :
	temporary_holder = number_1
	number_1 = number_3
	number_2 = temporary_holder

if number_2 > number_3 : 
	temporary_holder = number_2
	number_2 = numner_3
	number_3 = temporary_holder

print(f"The numbers in ascending order is {number_1} {number_2} {number_3}");
	