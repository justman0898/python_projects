import unittest
import encrypt_function

class TestEncryptFunction(unittest.TestCase):
	def test_that_encrypt_exist(self):
		encrypt_function.encrypt("word")
	def test_that_encrypt_works(self):
		actual =encrypt_function.encrypt("HelloWorld")
		self.assertEqual("UryybJbey", actual)