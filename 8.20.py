class BankAccount:
    def __init__(self,money=0):
        self.Balance=money+0.00
    def withdraw(self,money):
        self.Balance-=money
    def deposit(self, money):
        self.Balance+=money
    def balance(self):
        print('%.2f' %x.Balance)
