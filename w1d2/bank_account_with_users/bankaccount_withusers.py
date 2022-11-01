class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
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


# savings = BankAccount(.05, 1000)
# checking = BankAccount(.02, 5000)

# savings.deposit(10).deposit(20).deposit(40).withdraw(
#     600).yeild_interest().display_account_info()
# checking.deposit(100).deposit(200).deposit(400).withdraw(
#     60).yeild_interest().display_account_info()

# BankAccount.print_all_accounts()
# --------------User class------------------------


class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):

        self.account.deposit(100)

    def make_withdrawal(self, amount):

        self.account.withdrawal(100)

    def display_user_balance(self, amount):

        print(self.account.balance)

    def display_info(self):

        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")

    def enroll(self):
        
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):

        self.gold_card_points = self.gold_card_points - amount


# outer scope
# user = User("Boyd", "Lever", "boydlever@stanfordhacker.com", 34)
