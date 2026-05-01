import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# -database--
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    name TEXT PRIMARY KEY,
    balance REAL
)
""")

conn.commit()

# -classes-
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = self.load_account()

    def load_account(self):
        cursor.execute("SELECT balance FROM accounts WHERE name=?", (self.name,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None  # account doesn't exist yet

    def create_account(self, initial_deposit):
        cursor.execute(
            "INSERT INTO accounts (name, balance) VALUES (?, ?)",
            (self.name, initial_deposit)
        )
        conn.commit()
        self.balance = initial_deposit
        print("Account created successfully!")

    def update_balance(self):
        cursor.execute(
            "UPDATE accounts SET balance=? WHERE name=?",
            (self.balance, self.name)
        )
        conn.commit()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.update_balance()
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            self.update_balance()
            print(f"Withdrew ${amount}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# -lists the accounts-
def list_accounts():
    cursor.execute("SELECT name, balance FROM accounts")
    accounts = cursor.fetchall()

    print("\n--- All Accounts ---")
    if not accounts:
        print("No accounts found.")
    else:
        for name, balance in accounts:
            print(f"{name} - ${balance}")

# -main menu-
def main():
    print("\n========================")
    print("   SIMPLE BANK SYSTEM")
    print("========================")

    name = input("Enter your name: ")
    account = BankAccount(name)

    # Ceatre acc w/ intial deposit
    if account.balance is None:
        try:
            initial_deposit = float(input("Enter initial deposit: "))
        except:
            print("Invalid input, setting deposit to 0")
            initial_deposit = 0

        account.create_account(initial_deposit)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. List All Accounts")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            list_accounts()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

# -running--
if __name__ == "__main__":
    main()