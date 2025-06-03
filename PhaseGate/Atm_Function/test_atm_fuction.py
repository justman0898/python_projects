import atm_functions
import unittest

class TestAtmFunctions(unittest.TestCase):
	
	def setUp(self):
		atm_functions.account_balance.clear()
	
	def test_that_add_account_balance_exists(self):
		atm_functions.add_account_balance(20000)
	def test_add_account_balance(self):
		atm_functions.add_account_balance(20000)		
		self.assertEqual(20000, atm_functions.get_account_balance())
	def test_add_account_balance_with_negative(self):
		atm_functions.add_account_balance(-20000)		
		self.assertEqual("Cannot deposit Negative Numbers", atm_functions.add_account_balance(-20000))
	def test_withdraw_function_exists(self):
		atm_functions.add_account_balance(20000)
		atm_functions.withdraw(5000)
	def test_withdraw_function(self):
		atm_functions.add_account_balance(20000)
		atm_functions.withdraw(5000)
		self.assertEqual(14900, atm_functions.get_account_balance())
	def test_withdraw_function_withdraws_in_500(self):
		atm_functions.add_account_balance(20000)
		self.assertEqual("You can only withdraw in multiples of 500", atm_functions.withdraw(5100))
	def test_withdraw_function_removes_charges(self):
		atm_functions.add_account_balance(20000)
		atm_functions.withdraw(5000)
		self.assertEqual(14_900, atm_functions.get_account_balance())
	def test_withdraw_function_handles_20k_upwards(self):
		atm_functions.add_account_balance(20000)
		self.assertEqual("20K maximum limit", atm_functions.withdraw(21_000))
	def test_that_cannot_withraw_over_90_percent_of_account_balance(self):
		atm_functions.add_account_balance(20000)
		self.assertEqual("Cannot withdraw more than 90% of your balance", atm_functions.withdraw(19_000))
	def test_that_account_balance_cannot_be_less_than_100(self):
		atm_functions.add_account_balance(90)
		self.assertEqual("Account balance cannot be less than N100", atm_functions.add_account_balance(90))
	def test_get_withdrawals(self):
		atm_functions.add_account_balance(20000)
		atm_functions.withdraw(5000)
		atm_functions.withdraw(5000)
		expected = [5000,5000]
		self.assertEqual(expected, atm_functions.get_withdrawls())
		
		




