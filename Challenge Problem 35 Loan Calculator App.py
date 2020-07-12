#Fucntion Challenge 35:Loan Calculator App

def get_loan_info():
    """Get the basic information of the loan and store in a datadictionary"""
    #Create a blank dict to store the loan information
    loan={}
    loan['principal'] = float(input("Enter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: "))/100
    loan['monthly payment'] = float(input("Enter the desired monthly payment: "))
    loan['money paid'] = 0

    return loan

def show_loan_info(loan,number):
    """Display the current loan status"""
    print(f"----------Loan information after {number} 's months------------")
    for key,value in loan.items():
        print(key.title() + ":" + str(value))

def collect_interest():
    """Update laon for interest per month"""

def make_monthly_payment():
    """Simulate making a monthly payment to pay down the pricipal"""

def summarize_loan():
    """Display the results of paying off the loan"""

def create_graph():
    """Create a graph to show the relationship between principle and time"""

