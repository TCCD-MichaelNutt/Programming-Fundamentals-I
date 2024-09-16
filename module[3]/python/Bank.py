import Account

def menu(customer: Account):
    num_tries = 0
    limit = 3
    correct_pin = False

    while not correct_pin and num_tries <= limit:
        input("Enter your pin: ", pin)
        if pin == customer.pin:
            correct_pin = True
        else:
            num_tries += 1
    
    if not correct_pin:
        print("You've tried too many times!")
        return
    
    while True:
        input(
            "Enter your choice:\n" + 
            "1. Deposit\n" +
            "2. Withdraw\n" +
            "3. Check Balance" +
            "4. Print Deposit History\n" +
            "5. Exit", option
        )

        if option is 1:
            input("Enter deposit amount: ", amount)
            customer.deposit(pin, amount)
        elif option is 2:
            input("Enter withdraw amount: ", amount)
            customer.withdraw(pin, amount)
        elif option is 3:
            print(customer.balance)
        elif option is 4:
            customer.print_deposit_history()
        elif option is 5:
            return

test_account = Account("test name", "1234", 100.0)
menu(test_account)