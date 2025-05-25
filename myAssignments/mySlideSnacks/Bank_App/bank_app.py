accounts = []

def get_all_accounts(accounts):
	return accounts

def add_account(name,phone_number,balance=0.0):
	new_account = [name,phone_number,balance]
	
	for existing_account in accounts:
		if existing_account[1] == phone_number:
			raise ValueError("Phone number already Exists")	
	accounts.append(new_account)

