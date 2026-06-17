class Bankaccount:
    def __init__(self):
        self.balance = 0

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance-= amount

    def check_balance(self):
        print("Balance:", self.balance)


        acc = Bankaccount()
        acc.deposite(5000) 
        acc.withdraw(2000)

        acc.check_balance()      
