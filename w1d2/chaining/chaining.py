class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):

        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        return self

    def enroll(self):
        # add logic to check if they are a member
        # and  if true, print “User already a member”
        # or if false, return False.
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):

        self.gold_card_points = self.gold_card_points - amount
        return self


# outer scope
user1 = User("Boyd", "Lever", "boydlever@stanfordhacker.com", 34)
user2 = User("John", "A", "email@codingdojo.com", 21)
user3 = User("Billy", "B", "email@pythonisgreat.com", 27)
user1.display_info().enroll().spend_points(50)
user2.display_info().enroll().spend_points(50)
