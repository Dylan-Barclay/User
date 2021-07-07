class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

user1 = User('Adam Jones', 'adamjones@example.com')
user2 = User('Tim Randolf', 'randolftim@example.com')
user3 = User('Hazel May', 'bestdog@example.com')

user1.make_deposit(900).make_deposit(50).make_deposit(5).make_withdraw(300).display_user_balance()
user2.make_deposit(300).make_deposit(500).make_withdraw(100).make_withdraw(200).display_user_balance()
user3.make_deposit(100).make_withdraw(90).make_withdraw(5).make_withdraw(10).display_user_balance()