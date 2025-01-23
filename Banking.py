class Account:
    def __init__(self,balance):
        if balance >= 0.0:
            self.balance = balance
        else:
            self.balance = 0.0
            print("intial balance was invalid")
    def debit (self,damt):
        if damt > self.balance:
            print("Debit amount exceeded account balance.")
            return False
        else:
            self.balance = self.balance-damt
            return True
    def credit(self,camt):
        self.balance = self.balance+camt
    def getbalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self,balance,roi):
        super().__init__(balance)
        self.roi = roi
    def calculateInterest(self):
        return (self.balance*1*self.roi)/100
class CheckingAccount(Account):
    def __init__(self,balance,tfee):
        super().__init__(balance)
        self.tfee = tfee
    def debit(self,damt):
        res=super().debit(damt)
        if res:
            self.balance = self.balance-self.tfee
    def credit(self,camt):
        super().credit(camt)
        self.balance=self.balance-self.tfee
class CurrentAccount(Account):
    def __init__(self,balance,over_draft):
        super().__init__(balance)
        self.over_draft = over_draft
    def debit(self,damt):
        if damt>(self.balance+self.over_draft):
            print("Debit amount exceeded account balance.")
            return False
        else:
            self.balance = self.balance-damt
            return True
a1 = Account(-10000.00)
print(a1.getbalance()) 
a2 = Account(10000.00)
print(a2.getbalance())
a2.credit(10000.00)
print(a2.getbalance())
a2.debit(5000.00)
print(a2.getbalance())
a2.debit(20000.00)
print(a2.getbalance())
sa1 = SavingsAccount(100000.00,5.0)
print(sa1.getbalance())
sa1.credit(sa1.calculateInterest())
print(sa1.getbalance())
ca1 = CheckingAccount(100000.00,50.00)
print(ca1.getbalance())
ca1.credit(10000.00)
print(ca1.getbalance())
ca1.debit(5000.00)
print(ca1.getbalance())
ca1.debit(25000.00)
print(ca1.getbalance())
cu1 = CurrentAccount(100000.00,50000.00)
print(cu1.getbalance())
cu1.debit(5000.00)
print(cu1.getbalance())
cu1.debit(6000.00)
print(cu1.getbalance())
cu1.debit(2000.00)
print(cu1.getbalance())
cu1.debit(6000.00)
print(cu1.getbalance())
