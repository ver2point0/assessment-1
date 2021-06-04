class ChangeMaker:

	# __init__ method
	def __init__(self, item_cost, amount_paid):
		self.item_cost = item_cost
		self.amount_paid = amount_paid

		# self.change_needed computes to a negative integer
		self.change_needed = int((amount_paid * 100) - (item_cost) * 100)

		# currency dictionary
		self.currency_dict = {
			'$100 bill': 10000,
			'$50 bill': 5000,
			'$20 bill': 2000,
			'$10 bill': 1000,
			'$5 bill': 500,
			'$1 bill': 100,
			'quarter': 25,
			'dime': 10,
			'nickel': 5,
			'penny': 1,
		}

	# optimal_change method
	def optimal_change(self):
		# resulting change variable
		change = ""
		
		# more change is needed to complete payment
		if self.change_needed < 0:
			return f"The cost is ${self.item_cost} and the amount you paid is ${self.amount_paid}. Continue depositing ${(self.amount_paid - self.item_cost) * -1}."

		# exact change has been paid
		if self.change_needed == 0:
			return f"You've paid with exact change."

		# iterate through currency dictionary to count change and apply to {change} variable
		for key, value in self.currency_dict.items():
			count_change = 0
			
			if self.change_needed >= value:
				# The divmod() function returns a tuple containing the quotient and the remainder when argument1 (dividend is self.change_needed) is divided by argument2 (divisor is value)
				(biggest_number, self.change_needed) = divmod(self.change_needed, value)

				for i in range(0, biggest_number):
					count_change += 1

				if self.change_needed == 0 and key == "penny" and count_change > 1:
					change += f'{count_change} pennies.'
				elif self.change_needed == 0 and key != "penny" and count_change > 1:
					change += f'{count_change} {key}s.'
				elif self.change_needed == 0 and count_change == 1:
					change += f'{count_change} {key}.'
				elif self.change_needed > 0 and count_change == 1:
					change += f'{count_change} {key}, '
				else:
					change += f'{count_change} {key}s, '

		return f'The optimal change for an item that costs ${self.item_cost} with an amount paid of ${self.amount_paid} is {change}'