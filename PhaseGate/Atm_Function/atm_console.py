import atm_functions

print("=== Welcome to semi-colon Bank ===")
verification = True
while verification:
	account_balance = float(input("Enter account balance here: "))
	if account_balance >= 100:
		break
	else:
		continue

running = True
while running:
	print("""
1. Make Withdrawal
2. View all withdrawals
0. Quit
	""");
	user_input = input("Choose an option: ")
	match user_input:
		case "1":
			inwithdrawal = True
			while inwithdrawal:
				
				atm_functions.add_account_balance(account_balance)
				print("Your current balance ", atm_functions.get_account_balance())
				amount = float(input("Enter withdrawal amount here(in multiples of 500 and 1000): "))
				print(atm_functions.withdraw(amount))				
				print("Remaining balance: ",atm_functions.get_account_balance())

				print("""
				Continue ?
		
				1. Yes 		2. No
				""")
				user_input2 = input("Choose an option: ")
				match user_input2:
					case "1":
						inwithdrawal = True
					case "2":
						inwithdrawal = False
					case _:
						print("Invalid Selection")
		case "2":
			print(atm_functions.get_withdrawls())
		case "0":
			running = False
			


