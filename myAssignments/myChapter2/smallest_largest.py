integer_1 = int(input("Enter the first number: "))

integer_2 = int(input("Enter the second number: "))

integer_3 = int(input("Enter the third number: "))

largest = integer_1 ;
smallest = integer_1;

if integer_2 > largest:
	largest = integer_2;

if integer_3 > largest:
	largest = integer_3;

if integer_2 < smallest:
	smallest = integer_2;

if integer_3 < smallest:
	smallest = integer_3;

sum = integer_1 + integer_2 + integer_3 ;
product = integer_1 * integer_2 * integer_3
average = (integer_1 + integer_2 + integer_3) / 3 ;

print("The smallest is", smallest);
print("The largest is", largest);
print("The sum is", sum);
print("The average is", average);
print("The product is", product);





	
