class BankingCustomer:
	"Represents customer with name and balance"

	#internal dictionary with customers data
	allCustomers = {}

	#creating __init__ for customer initialization and adding him into allCustomers dictionary
	def __init__(self, name, balance = 0):
		"Customer initialization"
		self.name = name
		self.balance = balance
		BankingCustomer.allCustomers[self.name] = self.balance
		print("\nCustomer profile for {} has been created.".format(self.name))
		if BankingCustomer.allCustomers[self.name] == 0:
			print("{} hasn't placed any funds as initial deposit".format(self.name))
		else:
			print("{} has made an initial deposit of {} USD".format(self.name, BankingCustomer.allCustomers[self.name]))
	
	def deposit(self, amount):
		"Deposit processing"
		self.amount = amount
		print("\n{1} has deposited {0} USD into bank account.".format(self.amount, self.name))
		BankingCustomer.allCustomers[self.name]+= self.amount
		print("{}\'s new balance is {} USD.".format(self.name, BankingCustomer.allCustomers[self.name]))
	
	def withdrawal(self, amount):
		"withdrawal processing"
		self.amount = amount
		if self.amount > BankingCustomer.allCustomers[self.name]:
			print("\n{} wants to withdraw {} USD but doesn't have enough funds to perform this \
transaction.".format(self.name, self.amount))
		else:
			print("\n{} took {} USD from his account.".format(self.name, self.amount))
			BankingCustomer.allCustomers[self.name] -= self.amount
		print("{}\'s account balance is {} USD.".format(self.name, BankingCustomer.allCustomers[self.name]))
	
	def balanceCheck(self):
		"Balance check functonality"
		print("\n{1}\'s balance is {0} USD.".format(BankingCustomer.allCustomers[self.name], self.name))
	#class methods
	@classmethod
	
	def totalCustomers(cls):
		"Prints the current customer base."
		print("Bank has a customer base of {} customers".format(len(cls.allCustomers)))
	
	@classmethod
	
	def totalFunds(cls):
		"Prints the total amount of funds allocated on customer's accounts."
		print("Bank has in total {} USD stored on all customer's accounts.".format(sum(cls.allCustomers.values())))


customer1 = BankingCustomer("Mike")
customer1.deposit(500)
customer1.withdrawal(1000)
customer1.withdrawal(300)
customer1.balanceCheck()
customer2 = BankingCustomer("Jim", 1000)
customer2.balanceCheck()
print(BankingCustomer.allCustomers)

BankingCustomer.totalCustomers()
BankingCustomer.totalFunds()



