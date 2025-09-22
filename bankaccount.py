# TODO create class BankAccount

if __name__ == "__main__":
    # create BankAccount below this
    pass

class BankAccount:
    def __init__(self,balance = 0):
        self.balance=balance

    def deposit(self,n):
        if self.balance <0 :
            return self.balance
        self.balance+=n
        return self.balance

    def withdraw(self,n):
        if n>self.balance:
            return "Insefficent Funds"
        elif n<0:
            return self.balance

        return self.balance-n

    def get_balance(self):
        return self.balance