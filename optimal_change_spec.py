import unittest
from optimal_change import ChangeMaker

class OptimalChangeTest(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(ChangeMaker(62.13, 100).optimal_change(), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, 2 pennies.")

	def test_2(self):
		self.assertEqual(ChangeMaker(31.51, 50).optimal_change(), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, 4 pennies.")

	def test_3(self):
		self.assertEqual(ChangeMaker(100, 100).optimal_change(), "You've paid with exact change.")

	def test_4(self):
		self.assertEqual(ChangeMaker(1.00, 0.40).optimal_change(), "The cost is $1.0 and the amount you paid is $0.4. Continue depositng $0.6.")

	def test_5(self):
		self.assertEqual(ChangeMaker(0.04, 0.01).optimal_change(), "The optimal change for an item that costs $0.01 with an amount paid of $0.04 is 3 pennies.")


if __name__ == "__main__":
	unittest.main()