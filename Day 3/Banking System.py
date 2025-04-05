class InsufficientFundsError(Exception):

    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        try:
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient balance to complete the withdrawal.")
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: {self.balance}"
        except ValueError as ve:
            return f"Error: {ve}"
        except InsufficientFundsError as ife:
            return f"Error: {ife}"
        except Exception as e:
            return f"Error: An unexpected error occurred - {e}"


# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
print(account.withdraw(50))  # Should successfully withdraw and show remaining balance