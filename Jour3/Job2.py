class BankAccount:
    def __init__(self, number, name, firstname, balance, overdraft):
        self.__account_number = number
        self.__name = name
        self.__firstname = firstname
        self.__balance = balance
        self.__overdraft = overdraft

    def show_infos(self):
        print(f"Number: {self.__account_number} Name: {self.__name} "
              f"Firstname: {self.__firstname} Balance: {self.__balance} ")

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def payment(self, amount):
        self.__balance += amount
        print(f"Successfully transfer {amount} $")

    def withdraw(self, amount):
        if isinstance(amount, int) and amount > 0:
            if amount <= self.__balance or self.__overdraft:
                self.__balance -= amount
                print(f"Successfully withdraw {amount} $")
                if self.__balance < 0:
                    self.apply_bank_fees()
            else:
                print(f"Not enough money on account. Current balance: {self.__balance}")
        else:
            print("Error")

    def bank_transfer(self, account, amount):
        if amount <= self.__balance or self.__overdraft:
            self.__balance -= amount
            account.receive_tranfer(amount, self.__name)
            print(f'successfully transfer {amount}')
            if self.__balance < 0:
                self.apply_bank_fees()
        else:
            print(f"Not enough money on account. Current balance: {self.__balance}")

    def receive_tranfer(self, amount, name):
        self.__balance += amount
        print(f"Successfully receive {amount} from account {name}")

    def apply_bank_fees(self):
        fees = -self.__balance * (5 / 100)
        self.__balance -= fees
        print(f"Fees rise to : {fees} $")


bank_account_1 = BankAccount(1, "Biden", "Joe", 150, True)
bank_account_2 = BankAccount(1, "Trump", "Donald", 150, True)


# Test transfer


# bank_account_1.show_infos()
# bank_account_2.show_infos()
# bank_account_1.bank_transfer(bank_account_2, 300)
# bank_account_1.show_infos()
# bank_account_2.show_infos()


# Test Withdraw


# bank_account_1.show_infos()
# bank_account_1.withdraw(300)
# bank_account_1.show_infos()
