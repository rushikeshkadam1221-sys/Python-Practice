# ATM Simulator for check balance, withdraw, and Insufficient balance

balance = 10000 # Initial balance
withdraw = 2000 # Amount to withdraw

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful!");
    print("Remaining Balance:", balance);
else:
    print("Insufficient Balance!");