sum_number = 0
product = 1
largest = -2_000_000_000_000
smallest = 2_000_000_000_000


for numbers in range (1 , 5):

	num = int(input("Enter numbers: "))

	sum_number = sum_number + num

	average = sum_number / numbers

	product = product * num

	if num > largest:
		largest = num

	if num < smallest:
		smallest = num

print("The sum is " , sum_number)
print("The average is " , average)
print("The product is " , product)
print("The largest is " , largest)
print("The smallest is " , smallest)