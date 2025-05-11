num = int(input("Enter First Number: "))
num1 = int(input("Enter Second Number: "))
num2 = int(input("Enter Third number: "))

sum = num + num1 + num2
average = sum / 3
product = num * num1 * num2

largest = num
smallest = num

if (num1 > largest):
	largest = num1

if (num2 > largest):
	largest = num2

if (num1 < smallest):
	smallest = num1

if (num2 < smallest):
	smallest = num2

print("The sum of the number is ", sum)
print("The product of the number is ", product)
print("The average of the number is ", average)
print("The largest of the number is ", largest)
print("The smallest of the number is ", smallest)
