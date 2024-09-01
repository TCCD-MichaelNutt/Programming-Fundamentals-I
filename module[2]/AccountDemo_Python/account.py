
class Account:
    """
    Class definition of the Account class in Python that we created in C++.
    For this implementation I am also going to be using Python's Type Hinting feature. This allows
    you to provide a Type for each variable, if someone who is using your code is using an IDE it will
    give them an error should they try to pass a different type. This will not actually cause a runtime
    error, unless the type they pass is incompatible with the operations you are completing.
    """
    def __init__(
            self,
            customer_name: str = "Test Name",
            account_balance: float = 0.00,
            pin: str = "1234"
    ):
        """
        As mentioned in class, Python doesn't have the same kind of access modifiers that C++ does.
        Instead, if you intend for a variable or function to be private, you can prepend the name with
        a _. While someone using the library can still call the variable or function, IDEs will generate
        a warning that the variable or function was intended to be private.

        :param customer_name: The name of the customer.
        :param account_balance: The starting balance
        :param pin: The pin of the customer.
        """
        self._accountBalance = account_balance
        self._customerName = customer_name
        self._pin = pin

    def get_customer_name(self):
        return self._customerName

    def check_balance(self, pin: str) -> float:
        if pin == self._pin:
            return self._accountBalance

    def _update_balance(self, amount: float) -> None:
        self._accountBalance += amount

    def deposit(self, pin: str, amount: float) -> None:
        if pin == self._pin:
            if amount > 0:
                self._update_balance(amount)
            else:
                print("Invalid amount")

    def withdraw(self, pin: str, amount: float) -> None:
        if pin == self._pin:
            if amount < 0:
                self._update_balance(amount)
            else:
                print("Invalid amount")