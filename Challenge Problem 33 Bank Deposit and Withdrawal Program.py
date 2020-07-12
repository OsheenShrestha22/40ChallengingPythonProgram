def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print("\nWelcome to the Python First National Bankk")
    #Get user input
    name= input("\nHello!What is your name:").title().strip()
    savings= int(input("How much money would you like to set up your saving acoount with:"))
    checking =int(input("How much money would you like to set up your checking account with:"))

    #Build a dict that represents a  specific bank account
    bank_account = {

        "Name":name,
        "Savings":savings,
        "Checking":checking,
    }
    return bank_account

def make_deposite(bank_account,money,account):
    """Add money to a specific type of account"""
    bank_account[account] +=  money
    print(f"Deposited $ {money} into {bank_account['Name']}'s {account}")


def make_withdrawal(bank_account,money,account):
    """Withdraw money from a specific type of account"""
    if bank_account[account] - money >=0:
        bank_account[account]-= money
        print(f"Withdraw $ {money} from {bank_account['Name']}'s {account}")
    else:
        print(f" Sorry withdrawing $ {money} from you will have negative balance.")


def display_info(bank_account):
    """Display all key-value pair in a given bank account"""
    print("Current Account Information")
    for key, value in bank_account.items():
        if key == 'Name':
            print(f"{key} : {value}")
        else:
            print(f"{key}: ${value}")

#The main code
#Create a bank account

my_account = get_info()

running = True
while running:
    #Show the current state of the bank account
    display_info(my_account)

    #Get user input for the transaction information

    account_type = input("What account would you like to access (Savings or Checking) :").title()
    choice = input("What type of transaction would you like to make (Deposite or Withdrawal) : ").title()
    amount = float(input("How Much Money? : "))


    if account_type == 'Savings' or account_type == 'Checking':
        if choice == 'Deposite':
            make_deposite(my_account,amount,account_type)
        elif choice == 'Withdrawal':
            make_withdrawal(my_account,amount,account_type)
        else:
            print("\nI am sorry we cannot do that for you today.")
    else:
        print("\nI am sorry we cannot do that for you today.")


    #Allow user to make another transaction

    choice = input("Would you like to run the program again (y/n):").lower()
    if choice != 'y':
        print("Thankyou. GoodBye!")
        running = False
