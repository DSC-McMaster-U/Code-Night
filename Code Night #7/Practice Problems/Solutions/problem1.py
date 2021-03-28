def problem1(account_balance, num_transactions, credit_score):
    if credit_score < 300:
        x = 20
        y = 5
    else:
        x = 10
        y = 2
    if account_balance < 2500:
        account_balance -= x
    if num_transactions < 2 or num_transactions > 10:
        account_balance -= y*num_transactions
    return account_balance


print(problem1(2389.53, 13, 300))
