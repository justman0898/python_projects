

for side1 in range (1, 21):
	for side2 in range (side1, 21):
		for hypotenuse in range (1, 21):
			if side1**2 + side2 **2 == hypotenuse**2:
				print(f"{side1:>2}, {side2:>2}, {hypotenuse:>2}")
"""

for number in range(1, 5):
	print("the first loop runs 4 times")
	for number in range(1, 6):
		print("the second loop runs 5 times")
		for number in range(1, 7):
			print("the last loop runs 6 times")

"""
	