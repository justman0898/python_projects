withdrawals = []
account_balance = []
CHARGES = 100

def add_account_balance(amount):
	if amount < 0:
		return f"Cannot deposit Negative Numbers"
	else:
		if amount < 100:
			return f"Account balance cannot be less than N100"
		else:
			account_balance.append(amount)
	
	
def withdraw(amount):
	if amount < 0:
		return f"Cannot input negative amount"
	if amount % 500 == 0:
		if amount >= 20_000:
			return f"20K maximum limit"
		else:
			if amount >= 0.9 * account_balance[0]:
				return f"Cannot withdraw more than 90% of your balance"	
			else:
				account_balance[0] = (account_balance[0] - amount) - CHARGES
				withdrawals.append(amount)
				print("Transaction Successful")
				print("Withdrawal amount: ", amount)
				return f""
	else:
		return f"You can only withdraw in multiples of 500"
	

def get_account_balance():
	return account_balance[0]
def get_withdrawls():
	return withdrawals




