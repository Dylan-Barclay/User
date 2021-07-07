class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

user1 = User('Adam Jones', 'adamjones@example.com')
user2 = User('Tim Randolf', 'randolftim@example.com')
user3 = User('Hazel May', 'bestdog@example.com')

user1.make_deposit(900)
user1.make_deposit(50)
user1.make_deposit(5)
user1.make_withdraw(300)
user1.display_user_balance()
user2.make_deposit(300)
user2.make_deposit(500)
user2.make_withdraw(100)
user2.make_withdraw(200)
user2.display_user_balance()
user3.make_deposit(100)
user3.make_withdraw(90)
user3.make_withdraw(5)
user3.make_withdraw(10)
user3.display_user_balance()