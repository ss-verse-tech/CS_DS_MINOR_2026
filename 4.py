class Account:
    def __init__(self, bal):
        self.__bal = bal

    def deposit(self, deposit_Amount):
        return f"you have deposited rs {self.deposit_Amount} and your current balance is {self.__bal+deposit_Amount}"

    def show_balance(self):
        return f"your account balance is rs {self.__bal}"


c1 = Account(1000);
# c1.bal = 5
# print(c1.__bal)
print(c1.show_balance())
print(c1.deposit(500))