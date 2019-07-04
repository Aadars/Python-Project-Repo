class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print('your balance is {}'.format(self.balance))

    def deposite(self,deposite_amount):
        self.balance = self.balance + deposite_amount
        return 'Now your current balance is {} '.format(self.balance)


    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount :
            print(withdraw_amount)
            self.balance = self.balance - withdraw_amount
            return 'Now your current balance is {}'.format(self.balance)
        else:
            return 'sorry you dont have a sufficient balanve your balance is {}'.format(self.balance)
a=Account('Aadarsh',400)
dep=int(input('Enter the Amount for Deposite : '))
print(a.deposite(dep))
wthr=int(input('Enter Amount For Withdraw : '))
print(a.withdraw(wthr))
