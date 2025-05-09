#implementation guidelines
#global accounts dictionary
accounts={}

#function to create a new account
def create_account():
    acc_number=input("enter new account number:")
    if acc_number in accounts:
        print("account already exists")
        return
    name=input("enter account holder name:")
    accounts[acc_number]={
        "name":name,
        "balance":0,
        "transaction":[]
    }
print("account created successfully.")

#function to withdraw money
def withdraw_money():
    acc_number=input("enter account number:")
    print("account not found.")
    return
try:
    amount=float(input("enter amount to withdraw:"))
    if amount<=0:
        raise value 
    if accounts[acc.number]["balance"]<amount:
            print("insufficient balance.")
            return
    accounts[acc.number]["balance"]<amount
    accounts[acc.number]["transactions"].append
    {"type":"withdraw","amount":-amount,"date",datetime}
      print("withdraw successfull. ")
    except value error:
        print("invalid amount.")

#funtion to view transaction history
def transaction_history():
    acc_number=input("account_number")
    if acc_number not in account:
       print("account not found")
       return
       transaction=acounts[acc_number]["transaction"]
       if not transaction:
        print("no transaction found.")
        return
        print("\ntransaction history:")
        for t in transaction:
            print({t[date]}|amount:({amount}))
    
#main menu loop
def main():
    while true:
        print("/n====bank menu====")
        print("1.create account")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.check balance")
        print("5.transaction history")
        print("6.exit")
    choice=input("enter your choice")
    if choice=="1":
        create_account()
        elif choice=="2":
            deposit_money()
        elif choice=="3":
            withdraw_money()
        elif choice=="4"
            check_balance()
        elif choice=="5"
            transaction_history()
        elif choice=="6"
            exiting programme()
            break
        else:
            print("invalid process")
        






       


