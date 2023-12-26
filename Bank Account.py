class BankAccount:
    def __init__(self):
        self.balance=0
        print("Hello Welcome To KVK Bank")
    def login(self):
        account_login=int(input("Enter your Account Number(12 Digits);"))
    def password(self):
        account_password=(input("Enter your Password;"))
        print("Login Successfull ")
    def deposit(self):
        amount=float(input("Enter the Amount you wish to Deposit ₹ ;"))
        self.balance += amount
        print("\n Amount Deposited ₹;",amount)
    def withdrawal(self):
        amount=float(input("Enter the Amount you wish to Withdraw ₹; "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Amount you have Withdrawn ₹;",amount)
        else:
            print("\n Sorry..! Insufficient Account Balance.")
    def display(self):
        print("\n Net Available Balance=", self.balance)

ba1 = BankAccount()
ba1.login()
ba1.password()
ba1.deposit()
ba1.withdrawal()
ba1.display()