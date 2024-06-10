import time
class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type 

class Account:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transactions = [] 

    def validate_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        self.balance -= amount
        self.transactions.append(Transaction(amount, "Withdrawal"))
        print(f"{amount} is debited from your account")
        print(f"Your updated balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))
        print(f"{amount} is credited to your account")
        print(f"Your updated balance is {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        print("Transaction History:")
        for transaction in self.transactions:
            print(f"{transaction.type}: {transaction.amount}")

def main():
    password = "hashed_password"

    pin = int(input("Enter your ATM pin: "))
    account = Account(2001, 15000)  

    if account.validate_pin(pin):
        while True:
            print("""
                1. Balance
                2. Withdraw
                3. Deposit
                4. Transaction History
                5. Exit
            """)

            try:
                choice = int(input("Please enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                print(f"Your current balance is {account.check_balance()}")
            elif choice == 2:
                withdraw_amount = int(input("Enter amount to withdraw: "))
                account.withdraw(withdraw_amount)
            elif choice == 3:
                deposit_amount = int(input("Enter amount to deposit: "))
                account.deposit(deposit_amount)
            elif choice == 4:
                account.show_transactions()
            elif choice == 5:
                print("Thank you, Visit again!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Wrong pin. Please try again.")

if __name__ == "__main__":
    main()
