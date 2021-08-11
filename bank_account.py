class BankAccount:
    
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance -= amount
        else:
            self.balance -= (5+amount)
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+self.int_rate)
        else:
            print("Account overdrwan: No interests given")
        return self

account_1 = BankAccount(0.01)
account_2 = BankAccount(0.02,300)

print("Account 1")

# Make 3 deposits and 1 withdrawal for account_1, then calculate interest and display info

# Operation 1 
print("Operation 1")
account_1.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest().display_account_info()
# Operation 2
print("\nOperation 2")
account_1.withdraw(1000).yield_interest().display_account_info()

print("\nAccount 2")

# Make 2 deposits and 4 withdrawal for account_2, then calculate interest and display info

# Operation 1 
print("Operation 1")
account_2.deposit(100).deposit(200).withdraw(150).withdraw(150).withdraw(150).withdraw(150).display_account_info()
# Operation 2
print("\nOperation 2")
account_2.deposit(1000).yield_interest().display_account_info()