import time
print("Welcome to Prime Number App")

running = True

#Run the program as long as the user want

while running:
    #Get user input
    print("\nEnter 1 to determine if a specific number is prime :")
    print("\nEnter 2 to determine all prime number within a set range :")
    option = input("Enter your choice '1' or '2': ")

    #Determine if the single number is prime
    if option == '1':
        number = int(input("\nEnter a number to determine if it is prime or not"))

        #prime status check
        prime_status = True
        for i in range(2,number):
            if number%i == 0:
                prime_status = False
                break

        #Prime Summary
        if prime_status:
            print(f"{number} is prime!")
        else:
            print(f"{number} is not prime!")
    elif option == '2':
        l_bound = int(input("\nEnter the lower bound of your range:"))
        u_bound = int(input("\nEnter the upper bound of your range:"))

        prime = []

        #Get the current time
        start_time = time.time()

        #Check prime status of all numbers within l bound and u bound
        for prime_candidate in range(l_bound,u_bound+1):
            if prime_candidate > 1:
                prime_status = True
                for i in range(2,prime_candidate):
                    if prime_candidate%i ==0:
                        prime_status = False
                        break
            else:
                prime_status = False
            if prime_status:
                prime.append(prime_candidate)
        print(prime)

        #Get the current time
        end_time = time.time()

        #Determine the time the calculation took
        delta_time = round(start_time - end_time,4)
        print(f"\nCalculation took a total of {delta_time} seconds")
        print(f"The following number is prime between {u_bound} abd {l_bound} are")
        print("Press enter to continue")

        for primes in prime:
            print(primes)

    else:
        print("\nThat is not a valid option:")

    #Quit the program

    choice = input("Would you like to run the program again (y/n):").lower()
    if choice != 'y':
        running = False
        print("Thankyou for using the program! GoodBye!")