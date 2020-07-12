print("Welcome to the Factor Generator App")

running = True

#Run the program until the user quit
while running:
    #Get user input
    number=int(input("\nEnter a number to determine all factors of the number:"))

    factors = []
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)

    #Print out the factors
    print(f"\nFactors of {number} are")

    for factor in factors:
        print(factor)

    #Print a summary of the factors mathematically
    print("In summary:")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(number))

    choice = input("Run Again (y/n):").lower()
    if choice != 'y':
        running=False
        print("Thankyou for using the program.Have a great day.")
