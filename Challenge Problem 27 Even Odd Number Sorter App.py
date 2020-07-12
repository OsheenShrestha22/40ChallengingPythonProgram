print("Welcome to the Even Odd Number Sorter App")

running = True

#Run the program until the user quit
while running:
    #Get user input
    num_string=input("\nEnter a string of number separated by comma:")
    num_string = num_string.replace(' ','')
    num_list = num_string.split(",")
    print(num_list)

    evens = []
    odds = []

    print("\n ------Result Summary--------")
    for number in num_list:
        number = int(number)
        print(number)
        if number % 2 == 0:
            evens.append(number)
            print(str(number) + "is even")
        else:
            odds.append(number)
            print(str(number) + "is odd")

        evens.sort()
        odds.sort()

        #Show the even numbers
        print(f"The following {len(evens)} numbers are even:")

        for even in evens:
            print(f"\t{even}")

        # Show the even numbers
        print(f"The following {len(odds)} numbers are odd:")

        for odd in odds:
            print(f"\t{odd}")

        choice = input("Would you like to run the program again (y/n):").lower()
        if choice != 'y':
            running =False
            print("Thankyou for using the program! GoodBye!")





