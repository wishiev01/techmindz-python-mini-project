
#banking system using file handling

import os
from datetime import datetime

ACCOUNT_FILE = "vishie4455.txt"
USERNAME = "vishnu"
ACCOUNT_NUMBER = "vishie4455"


def initialize_account():
    if not os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, 'w') as f:
            f.write("Account Holder: vishnu\n")
            f.write("Account Number: vishie4455\n")
            f.write("Balance: 0\n")
            f.write("Transactions:\n")
        print("Account initialized successfully.")


def get_balance():
    with open(ACCOUNT_FILE, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("Balance:"):
                return float(line.strip().split(":")[1])
    return 0.0


def update_balance(new_balance):
    with open(ACCOUNT_FILE, 'r') as f:
        lines = f.readlines()
    with open(ACCOUNT_FILE, 'w') as f:
        for line in lines:
            if line.startswith("Balance:"):
                f.write(f"Balance: {new_balance}\n")
            else:
                f.write(line)


def log_transaction(action, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ACCOUNT_FILE, 'a') as f:
        f.write(f"{now} - {action}: {amount}\n")


def deposit(amount):
    balance = get_balance()
    new_balance = balance + amount
    update_balance(new_balance)
    log_transaction("Deposit", amount)
    print(f"Deposited ₹{amount}. New balance: ₹{new_balance}")


def withdraw(amount):
    balance = get_balance()
    if amount > balance:
        print("Insufficient balance.")
        return
    new_balance = balance - amount
    update_balance(new_balance)
    log_transaction("Withdraw", amount)
    print(f"Withdrew ₹{amount}. New balance: ₹{new_balance}")


def check_balance():
    balance = get_balance()
    print(f"Current Balance: ₹{balance}")


def main():
    initialize_account()
    while True:
        print("\n===== Banking System =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: ₹"))
            deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: ₹"))
            withdraw(amt)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Exiting banking system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
