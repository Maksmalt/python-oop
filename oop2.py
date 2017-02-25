class BankingCustomer:
	"Represents customer with name and balance"

	def __init__(self, name, balance = 0):
		"Customer initialization"
		self.name = name
		self.balance = balance
		print("Customer profile for {} has been created.\n".format(self.name))

	def withdrawal(self, amount):
		"withdrawal processing"
		self.amount = amount

		if self.amount > self.balance:
			print("{} wants to withdraw {} USD but he has not enough funds to perform this \
				transaction.\n".format(self.name, self.amount))
		else:
			print("{} USD were taken from the account.\n".format(self.amount))
			self.balance -= self.amount

	def deposit(self, amount):
		"withdrawal processing"
		self.amount = amount
		print("{1} has deposited {0} USD into bank account.\n".format(self.amount, self.name))
		self.balance += self.amount

	def balanceCheck(self):
		print("{1}\'s balance is {0} USD.\n".format(self.balance, self.name))

customer1 = BankingCustomer("Mike")
customer1.balanceCheck()
customer1.deposit(1000)
customer1.balanceCheck()
customer1.withdrawal(1500)
customer1.balanceCheck()
print()
customer2 = BankingCustomer("Jim")
customer2.balanceCheck()

customers = [customer1, customer2]
print("We have {} customers in our Bank and their balances are:".format(len(customers)))
for customer in customers:
		customer.balanceCheck()

'''
	@classmethod

	def balanceCheck(cls):
		"Print the current balance"
		print("Balance is {} USD.\n".format(cls.balance))
'''