print("Welcome to the Voter Registration App")

name = str(input("\nPlease enter your name:"))
age = int(input("Please enter your age:"))
parties = ['Republican','Democratic','Independent','Libertarian','Green']

if age > 17:
    print(f"Congratulations {name}!You are old enough to register to vote:")
    print("Here is a list of political parties to join:")

    #Display the political party
    for party in parties:
        print(f"\t{party}")

    #Choose your party
    choosen_party = str(input("\nWhat party would you like to join:"))

    if choosen_party in parties:
        print(f"Congratulation {name}! You have joined the {choosen_party} Party")
        if choosen_party =='Republican' or choosen_party =='Democratic' :
            print("This is a majour party!")
        elif choosen_party =='Independent':
            print(f"You are Independent Person")
        else:
            print("This is not a given party!")
else:
    print("You are not old enough to vote!")