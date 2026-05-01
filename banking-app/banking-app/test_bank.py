import unittest
from banking_app import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        account = BankAccount("test1")
        account.balance = 0
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = BankAccount("test2")
        account.balance = 100
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_overdraft(self):
        account = BankAccount("test3")
        account.balance = 50
        account.withdraw(100)
        self.assertEqual(account.balance, 50)

if __name__ == "__main__":
    unittest.main()