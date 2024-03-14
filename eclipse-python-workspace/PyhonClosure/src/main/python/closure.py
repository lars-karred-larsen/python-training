'''
Created on Mar 13, 2024

@author: student
'''
def create_account(initial_balance=0):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return f"Deposited {amount}. New balance: {balance}."
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return f"Withdrawn {amount}. New balance: {balance}."
        else:
            return "Insufficient funds."
        
    def check_balance():
        return f"Current balance: {balance}."
    
    def yet_another_check_balance():
        return f"Current balance: {balance}."
    
    return deposit, withdraw, check_balance, yet_another_check_balance
 
# Create a closure for a bank account with an initial balance of 1000
account_deposit, account_withdraw, account_balance, account_balance2 = create_account(1000)
 
# Deposit and withdraw money and check balance
print(account_balance())
print(account_deposit(500))
print(account_withdraw(200))
print(account_balance())
print(account_withdraw(1500))

# Try with different names
first_sub_method, the_second_sub_method, and_the_third, plus_forth = create_account(1000)
 
print("\nUsing other variable names:\n*************************")
print(and_the_third())
print(first_sub_method(500))
print(the_second_sub_method(200))
print(plus_forth())
print(the_second_sub_method(1500))
