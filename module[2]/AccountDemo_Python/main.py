import account

test_account: account.Account = account.Account(
    "Test Customer",
    100.00,
    "2134"
)

test_account.deposit("2134", 20)
print(test_account.check_balance("2134"))
test_account.withdraw("2134", -20)
print(test_account.check_balance("2134"))
print(test_account.get_customer_name())