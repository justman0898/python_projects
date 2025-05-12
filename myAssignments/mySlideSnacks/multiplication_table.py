
print(" " * 10 + "Multiplication Table")
print(" " * 4, end="")
for each in range (1, 10):
	print(f"{each:>3}", end=" ")
print()
print(" "*4 + "-" * 36)
product = 0
for counter in range (1, 10):
	print(f"{counter:>2} |", end="")
	for count in range (1,10):
		product = counter * count
		print(f"{product:>3}", end=" ")
	print()	
