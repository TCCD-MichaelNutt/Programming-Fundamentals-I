"""
In this example I am using the optional type hinting, 
ex name: str hints that it is looking for a string

This does not cause the function to crash if a value other than a string is passed,
it will just tell IDEs what the function is expecting
"""

class Account:
    def __init__(self, name: str, pin: str, starting_balance: float):
        self.name = name
        self.pin = pin
        self.balance = starting_balance if starting_balance >= 0 else 0
        self.deposit_history = [starting_balance]

    def deposit(self, pin: str, amount: float):
        result = 0

        while pin is not self.pin:
            input("Invalid PIN\nTry again: ", pin)
        
        if amount > 0:
            result = updateBalance(amount)
            if result == 0:
                print("Deposit successful") # adds a newline automatically
            elif result == 1:
                print("Deposit failed")
            else:
                print("You shouldn't get here")

        return

    def withdraw(self, pin: str, amount: float):
        result = 0

        while pin is not self.pin:
            input("Invalid PIN\nTry again: ", pin)
        
        if amount < 0:
            result = updateBalance(amount)
            if result == 0:
                print("Withdraw successful") # adds a newline automatically
            elif result == 1:
                print("Withdraw failed")
            else:
                print("You shouldn't get here")

        return

    def update_balance(self, amount: float) -> int:
        self.balance += amount
        self.deposit_history.append(amount)
        return 0

    def print_deposit_history(self):
        for deposit in self.deposit_history:
            print(deposit)