def addition(num1,num2):
    add = num1+num2
    print(f"The sum of {num1} and {num2} is {add}")
    return str(num1) + "+" + str(num2) + '=' + str(add)

def substraction(num1,num2):
    substract = num1 - num2
    print(f"The difference of {num1} and {num2} is {substract}")
    return str(num1) + "-" +str(num2)  + '='+ str(substract)

def multiplication(num1,num2):
    multiply = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {multiply}")
    return str(num1) + "*" +str(num2)  + '='+ str(multiply)

def division (num1,num2):
    if num2 != 0:
        division = num1/num2
        print(f"The division of {num1} and {num2} is {division}")
        return str(num1) + "/" +str(num2)  + '=' + str(division)
    else:
        print("You cannot divide by zero")
        return "Div Error"

def exponential(num1,num2):
    power = round(num1**num2,4)
    print(f"The exponential of {num1} and {num2} is {power}")
    return str(num1) + "**" +str(num2)  + '='+ str(power)


print("Welcome to the Python Calculator App")


history = []
running = True
while running:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    choose = input("Enter an operation (addition,substraction,multiplication,division, or exponentiation:)")
    if choose == 'addition':
        result = addition(num1, num2)

    elif choose == 'substraction':
        result = substraction(num1, num2)

    elif choose == 'multiplication':
        result = division(num1, num2)

    elif choose == 'division':
        result = multiplication(num1, num2)
    else:
        print("This is not a valid operation:Try again")
        result = "OPP ERROR"

    history.append(result)

    choice = input("Would you like to run the program again (y/n):").lower()
    if choice != 'y':
        print("\nCalculation Summary: ")
        for calc in history:
            print(calc)
        print("Thankyou for using the python Calcaultor App! GoodBye!")
        running =False