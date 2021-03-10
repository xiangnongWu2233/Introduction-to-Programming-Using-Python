class BankAccount2:
    def __init__(self,money=0):
        if money<0:
            raise ValueError('Illegal balance')
        self.Balance=money
    def withdraw(self,money):
        if money>self.Balance:
            raise ValueError('Overdraft')
        self.Balance-=money
    def deposit(self, money):
        if money<0:
            raise ValueError('Negative deposit')
        self.Balance+=money
    def balance(self):
        print('%.2f' %x.Balance)
