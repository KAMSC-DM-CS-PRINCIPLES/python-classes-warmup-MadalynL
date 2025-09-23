# TODO create class BankAccount



class BankAccount:
    def __init__(self,balance = 0):
        self.balance=balance

    def deposit(self,n):
        if self.balance <0 :
            return "can not be negative"
        self.balance+=n
        return self.balance

    def withdraw(self,n):
        if n>self.balance:
            return "Insufficient Funds"
        elif n<0:
            return self.balance
        self.balance = self.balance - n
        return self.balance

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
        # create BankAccount below this
    bank = BankAccount(100)
    print(bank.deposit(30))
    print(bank.withdraw(30))
    print(bank.get_balance())

