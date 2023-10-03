class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance} units.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount} units. Current balance: {self.balance} units.")
        else:
            print("Insufficient balance.")

def login(accounts):
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if account_number in accounts and pin == accounts[account_number]['pin']:
        return accounts[account_number]['account']
    else:
        print("Invalid account number or PIN.")
        return None

def main():
    accounts = {
        '123456789': {'pin': '1234', 'account': BankAccount('123456789', '1234')},
        '987654321': {'pin': '4321', 'account': BankAccount('987654321', '4321', 1000)}
    }

    account = login(accounts)
    if account is None:
        return

    while True:
        print("\n===== Banking Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
