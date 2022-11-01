#learn platform solution
class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

BankAccount.print_all_accounts()

# #bank account code with errors that I wrote
# class BankAccount:
#     bankbalance = 10000000 #10 million dollars

#     def __init__(self, int_rate=0.01, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.bankbalance += balance

#     def deposit(self, amount):
#         deposit(self) = deposit(self) + amount
#         return self

#     def withdraw(self, amount):
#         withdraw(self) = withdraw(self) - amount
#         if withdraw(self) < amount:
#         print("Insufficient funds: Charging a $5 fee")
#         balance = balance - 5
#         return self

#     def display_account_info(self):
#         print(f"Your current balance is : ${balance}")
#         return self

#     def yield_interest(self):
#         if balance > 0:
#         balance = balance + balance * int_rate
#         return self

# @classmethod
#     def bankaccount_balance(cls):
#         print(f"There's ${cls.bankbalance} in the bank.")


# # Create accounts
# BankAccount1 = BankAccount(0.01, 1000)
# BankAccount2 = BankAccount(0.01, 30000)
# BankAccount1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()
# BankAccount2.desposit(1000).deposit(2000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
