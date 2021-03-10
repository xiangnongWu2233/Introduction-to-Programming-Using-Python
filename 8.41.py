class Negative_BalanceError(Exception):
    pass
class OverdraftError(Exception):
    pass
class DepositError(Exception):
    pass
class BankAccount3:
    def __init__(self,money=0):
        if money<0:
            raise Negative_BalanceError('Account created with negative balance %d' %money)
        self.Balance=money
    def withdraw(self,money):
        if money>self.Balance:
            raise OverdraftError('Operation would result in negative balance %d' %(self.Balance-money))
        self.Balance-=money
    def deposit(self, money):
        if money<0:
            raise DepositError('Negative deposit %d' %money)
        self.Balance+=money
    def balance(self):
        print('%.2f' %x.Balance)
