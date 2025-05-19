import divisor_function
import unittest

class TestDivisorFunction(unittest.TestCase):
	def test_that_divisor_function_exists(self):
		divisor_function.get_multiples()	
	def test_only_numbers_divisible_by_divisor_is_returned(self):
		actual = divisor_function.get_multiples(2,10,6, divisor=2)
		expected = (2, 10, 6)
		self.assertEqual(actual, expected)
	def test_with_numbers_not_divisible_by_divisor(self):
		actual = divisor_function.get_multiples(3,9,5, divisor=2)
		expected = "No Multiple Found"
		self.assertEqual(actual, expected)
	def test_to_ensure_filtering_works(self):
		actual = divisor_function.get_multiples(3,9,5,4,2,8,7, divisor=2)
		expected = (4,2,8)
		self.assertEqual(actual, expected)
	def test_to_handle_empty_input(self):
		actual = divisor_function.get_multiples()
		expected = "No Multiple Found"
		self.assertEqual(actual, expected)
	def test_that_default_divisor_is_applied(self):
		actual = divisor_function.get_multiples(2,4,5,7)
		expected = (2,4)
		self.assertEqual(actual, expected)
	def test_that_assigned_divisor_is_applied(self):
		actual = divisor_function.get_multiples(2,4,5,7, divisor=4)
		expected = (4,)
		self.assertEqual(actual, expected)
	def test_that_function_works_with_negative_numbers(self):
		actual = divisor_function.get_multiples(-2,-4,5,7)
		expected = (-2, -4)
		self.assertEqual(actual, expected)
	def test_that_guard_against_zero_and_non_integer_as_divisor_works(self):
		actual = divisor_function.get_multiples(2,4,5,7, divisor=0)
		expected = "Error divisor cannot be zero or must be a number"
		self.assertEqual(actual, expected)
	def test_that_function_can_handle_non_integer_inputs(self):
		actual = divisor_function.get_multiples("a",4,5,7)
		expected = "Not a number"
		self.assertEqual(actual, expected)

	



