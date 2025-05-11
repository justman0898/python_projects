purchase_amount = int(input("How much was your total amount: "))
discount = 0

if purchase_amount >= 1_000:
	if purchase_amount >= 1_000 and purchase_amount <= 10_000:
		discount = purchase_amount * 0.05
		price = purchase_amount - discount
		print(f"You recieved a 5% discount and new amount is ${price:,}")

	elif purchase_amount >= 10_000 and purchase_amount <= 50_000:
		discount = purchase_amount * 0.1
		price = purchase_amount - discount
		print(f"You recieved a 10% discount and new amount is ${price:,}")
	elif purchase_amount > 50_000:
		discount = purchase_amount * 0.2
		price = purchase_amount - discount
		print(f"You recieved a 20% discount and new amount is ${price:,}")
else: 
	print("Enter an amount within range.")