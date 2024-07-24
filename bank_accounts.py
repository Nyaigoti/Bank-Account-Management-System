class BalanceException(Exception):
    pass

class bankAccount:
    def __init__ (self, accName, initialAmount):
        self.balance = initialAmount
        self.name = accName
        
        print(f"\nAccount name '{self.name}' is created.\nBalance: ${self.balance:.2f}")
        
    def getBalance (self):
        print(f"\nAccount '{self.name}' balance is ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit successful.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw successful")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
    def transaction(self, amount, accName):
        try:
            print("\n***************\nBeginning transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            accName.deposit(amount)
            print("\nTransfer complete...✅\n***************")
        except BalanceException as error:
            print(f"\nTransfer interrupted..❌ {error}") 
            
class interestRewardAcc(bankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit successful")
        self.getBalance()   
        
            
        