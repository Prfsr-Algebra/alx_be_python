class BankAccount:
    """A class to represent a simple bank account."""
    
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

