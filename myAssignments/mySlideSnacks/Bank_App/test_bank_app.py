import bank_app
import unittest

class TestBankApp(unittest.TestCase):
	def setUp(self):
		bank_app.accounts.clear()
	def test_that_get_all_accounts_exists(self):
		bank_app.get_all_accounts(bank_app.accounts)	
	def test_get_all_accounts(self):		
		bank_app.add_account("Hilary","09068325094", 8000)
		bank_app.add_account("Wande","09068325095", 700)
		bank_app.add_account("Hilary","09068325096", 1000)
		self.assertListEqual([["Hilary","09068325094", 8000],["Wande","09068325095", 700],["Hilary","09068325096", 1000]], bank_app.get_all_accounts(bank_app.accounts))	
	def test_that_get_all_accounts_returns_empty_list(self):
		self.assertListEqual([],bank_app.get_all_accounts(bank_app.accounts))
	def test_that_get_all_accounts_returns_account_in_order_of_creation(self):
		bank_app.add_account("Han","08068325095", 1700.00)
		bank_app.add_account("Hilary","09068325094", 1000.00)
		bank_app.add_account("Wande","09068325093", 700.00)
		bank_app.add_account("Smith","09168325092", 12000.00)
		self.assertListEqual( [["Han","08068325095", 1700.00],["Hilary","09068325094", 1000.00],["Wande","09068325093", 700.00],["Smith","09168325092", 12000.00]], bank_app.get_all_accounts(bank_app.accounts) )	
	def test_that_add_account_function_exists(self):
		bank_app.add_account("Hilary","09068325094", 0.0)
	def test_that_add_account_function_adds_new_account(self):
		bank_app.add_account("Hilary","09068325094", 400)		
		self.assertListEqual(bank_app.accounts[0], ["Hilary", "09068325094", 400])
	def test_that_balance_defaults_to_zero(self):
		bank_app.add_account("Hilary","09068325094")
		self.assertListEqual(bank_app.accounts[0], ["Hilary", "09068325094", 0.0])	
	def test_that_phone_numbers_are_unique(self):		
		bank_app.add_account("Hilary","09068325094", 1000.00)
		self.assertRaises(ValueError, bank_app.add_account,"James","09068325094", 1700.00)
	
	
	
	
		