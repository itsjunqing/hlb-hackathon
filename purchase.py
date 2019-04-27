import copy

class Purchase:

	def __init__(self, target):
		self.target = target
		self.balance = copy.deepcopy(target)
		self.sold = False
		self.contributors = 0

	def valid_purchase(self, amount):
		if self.balance - amount >= 0:
			return True
		return False

	def make_purchase(self, amount):
		if self.valid_purchase(amount):
			if self.balance - amount == 0:
				self.sold = True
			self.balance -= amount
			self.contributors += 1
			return True
		return False
