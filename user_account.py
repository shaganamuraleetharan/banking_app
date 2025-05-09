#customer_inputs
def customer_information():
    name=str (input("enter your name:"))
    address=input("enter your address")
    user_id=input("enter user id:")
    user_id_password=input("enter user id password:")
    return[name,address,user_id,user_id_password]

def creat_customer():
    customer=customer_information()
   with open("customer.txt","a")as file :
   file.write("customer_name\t")
    file.write("customer_address")
    file.write("\n")
    file.write(f"{customer[0]}\t\t\t{customer[1]}\t")
    file.write("\n")
create_customer()
def create_users():
   customer=customer_information()
   with open("users.txt","a")as file:
   file.write("user_name\t")
   file.write("user_id_password")
   file.write("\n")
   file.write(f"{customer[2]}\t\t\t{customer[3]}\t")
   file.write"\n"
create_users()
with open customer.txt","a")as customer_file,open("users.txt","a")as user_file:

#deposit_money
def deposit_money(account_id,balance,amount):
    if amount<=0:
        print("invalid amount")
        return balance
    balance+=amount
    print("deposited ${amount}.new balance is ${balance}.")
    print("deposit successful.")

#withdraw_money
def __init__(self,account_number,balance=0):
    self.account_number=account-account_number
    self.balance=balance
    def withdraw(balance,amount):
        if amount<=balance:
            print("withdraw amount must be positive")
             elif amount >self. balance:
        print("insufficient funds.")
    else:
        self.balance-=amount
        print("withdrawal sucessful")
    def get_balance(self):
        return self.balance
    def get_transactions(self):
        return self.transactions

#check balance
def_init_(self,account_number,balance=0)
    self.account_number=account_number
    self.balance=balance
def check|_balance(self):
    return "current balance for account{self.account_number}:${self.balance:}"

#transaction history
def_init_("self,amount,transaction,description"class):
   self.date=datetime.()
   self.amount=amount
   self.type=transaction_type

   self.description=description
def to_dict(self):
    return
   {"date":self.date
    "amount":self.amount
    "type":self.type
    "description":self.description}

def_init_(self,user_id):
    self.user_id=user_id
    self.transactions[]

def deposit(self,amount,description=""):
    self.transactions.append(transaction(amount,"deposit",description))

def get_transaction_history(self,start_date,end_date,transaction_type):
    results=[]
    for t in self.transactions:
        if start_date and t.date<end_date:
            continue
        if transaction_type and t.type and t.type !=transaction_type:
            continue
        results.append(t)
        return results
    
    def export_transaction_to(self,filename):
        with open(filename,mode='w',newline='')as file:
            writer.header()
            for t in self.transactions:
                writer.writerow(t.to_dict())

#menu-driven interface
def_init_("self,amount<transaction_type,description"):
     self.date=datetime.now()
     self.amount=amount
     self.type=transaction_type
     self.description=description

def to_dict(self):
    return{
        "date":self.date,
        "amount":self.amount,
        "type":self.type,
        "description":self.description}

def_init_(self,user_id)
    self.user_id=user_id
    self.balance=0
    self.transaction=[]

def deposit(self,amount,description="deposit"):
    self.balance+=amount
    self.transactions.append(transcation(amount,"deposit",description))

    def withdraw(self,amount,description="withdraw")
    if amount>self.balance:
        print("insufficiant balance.")
        return
    self.balance=amount
    self.transactions.append(transaction(-amount,"withdrawa",description))

def get_balance(self):
    retrun self.balance

def show_transaction_history(self):
    if not self.transations:
        print("no transaction found.")
        return
    print("\ntransaction history")
    for t in self.transactions:

def main ():
    account=None
    while true:
        print("\n====bank menu====")
        print("1.create account")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.check balance")
        print("5.transaction history")
        print("6.exit")

chioce = input("enter your chioce (1-6):")

if choice=="1":
    user_id=input("enter user id:")
    account=account(user_id)
    print("account created successfully.")
    
elif choice=="2":
    if amount:
        amount =float(input("enter amount to deposit:"))
        account:deposit(amount)
        print("deposit sccessfully")
    else:
        print("account created successfullu.")

elif choice=="3":
    if account:
        amount=float(input("enter amount to withdraw:"))
        account.withdraw(amount)
    else:
        print("withdraw sucessful.")

elif choice=="4":
    if account:
    else:
        print("current balance:{account.get_balance()}")
    else:
        print("check balance.")

elif choice=="5":
    if account:
        account.show_transaction_history()
    else:
        print("show transaction history.")

elif choice=="6":
    print("exiting program.")
    break

else:
    print("invalid choice.enter a number from 1to 6.")

if_name_=="main":
   main()


        






    
        
    












