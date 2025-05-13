import datetime
import os

# ------------------------------Make new account number-----------------------
def generate_account_number():
    if not os.path.exists('account_numbers.txt'):
        with open('account_numbers.txt', 'w') as f:
            f.write('1001')
    
    with open('account_numbers.txt', 'r+') as f:
        current = int(f.read().strip())
        new = current + 1
        f.seek(0)
        f.write(str(new))
    
    return str(current)

# ----------- Save new account details--------------------
def write_account_details(acc_no, name, balance):
    with open('AccountDetails.txt', 'a') as f:
        f.write(f"{acc_no}|{name}|{balance}\n")

# --------------Save transaction log--------------------
def write_transaction(acc_no, txn):
    with open('transactions.txt', 'a') as f:
        f.write(f"{acc_no}|{txn}\n")

# ------------Admin creates user account----------------------
def createAccount():
    name = input("Enter Your Full Name: ").strip().upper()
    if name == '':
        print("Name cannot be empty.......")
        return

    try:
        balance = float(input("Enter Initial Balance: "))
        if balance < 0:
            print("Balance must be 0 or more.....")
            return
    except:
        print("Invalid input......")
        return

    acc_no = generate_account_number()
    username = "user" + acc_no
    password = "pass" + acc_no

    with open('credentials.txt', 'a') as f:
        f.write(f"{username}:{password}:user\n")

    
    write_account_details(acc_no, name, balance)

  
    write_transaction(acc_no, f"Account opened with Rs.{balance}")

    print("Account Created Successfully......")
    print("Account Number:", acc_no)
    print("Username:", username)
    print("Password:", password)

# ------------------------Deposit function---------------------
def depositMoney():
    acc_no = input("Enter Account Number: ").strip()

   
    if not os.path.exists('AccountDetails.txt'):
        print("No accounts found.")
        return

    lines = []
    found = False
    new_balance = 0.0

    with open('AccountDetails.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split('|')
        if parts[0] == acc_no:
            found = True
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    return
            except:
                print("Invalid amount.")
                return

            balance = float(parts[2])
            new_balance = balance + amount
            lines[i] = f"{acc_no}|{parts[1]}|{new_balance}\n"
            break

    if not found:
        print("Account not found.")
        return

    
    with open('AccountDetails.txt', 'w') as f:
        f.writelines(lines)

  
    txn = f"Deposited Rs.{amount} on {datetime.datetime.now()}"
    with open('transactions.txt', 'a') as f:
        f.write(f"{acc_no}|{txn}\n")

    print("Deposit Successful.")

# ------------------Withdraw function--------------------------
def withdrawMoney():
    acc_no = input("Enter Account Number: ").strip()

    
    if not os.path.exists('AccountDetails.txt'):
        print("No accounts found.")
        return

    lines = []
    found = False
    new_balance = 0.0

    with open('AccountDetails.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split('|')
        if parts[0] == acc_no:
            found = True
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    return
            except:
                print("Invalid amount.")
                return

            balance = float(parts[2])
            if amount > balance:
                print("Not enough balance.")
                return
            new_balance = balance - amount
            lines[i] = f"{acc_no}|{parts[1]}|{new_balance}\n"
            break

    if not found:
        print("Account not found.")
        return

   
    with open('AccountDetails.txt', 'w') as f:
        f.writelines(lines)

    
    txn = f"Withdrew Rs.{amount} on {datetime.datetime.now()}"
    with open('transactions.txt', 'a') as f:
        f.write(f"{acc_no}|{txn}\n")

    print("Withdraw Successful.")

# ------------------------Check balance--------------------------------
def checkBalance():
    acc_no = input("Enter Account Number: ").strip()

    # Read from AccountDetails.txt
    if not os.path.exists('AccountDetails.txt'):
        print("No accounts found.")
        return

    with open('AccountDetails.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split('|')
        if parts[0] == acc_no:
            print("Your Balance is Rs.", parts[2])
            return

    print("Account not found.")

# ----------------------------Show transactions------------------------------
def transactionHistory():
    acc_no = input("Enter Account Number: ").strip()

    # Read from transactions.txt
    if not os.path.exists('transactions.txt'):
        print("No transactions found.")
        return

    with open('transactions.txt', 'r') as f:
        lines = f.readlines()

    print("Transaction History:")
    for line in lines:
        parts = line.strip().split('|')
        if parts[0] == acc_no:
            print("-", parts[1])

# -------------------User menu--------------------
def userMenu():
    while True:
        print("\nMenu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Logout")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            createAccount()
        elif choice == '2':
            depositMoney()
        elif choice == '3':
            withdrawMoney()
        elif choice == '4':
            checkBalance()
        elif choice == '5':
            transactionHistory()
        elif choice == '6':
            break
        else:
            print("Invalid option.......")

userMenu()
