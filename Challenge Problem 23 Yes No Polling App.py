print("Welcome to the Yes or No Polling App")

issue = str(input("What is the yes or no issue you will be voting on today:"))
voter_num = int(input("What is the number of voters you will allow on the issue:"))
password = str(input("Enter a password for polling results:"))

yes =0
no =0
result ={}
for i in range(voter_num):
    name =input("Enter your full name:")
    if name in result.keys():
        print("Sorry it seems someone with that name has already voted")
    else:
        print(f"Here is our issue {issue}")
        choice =input("What do you think..yes or no:").lower()
        if choice == 'yes':
            choice = 'yes'
            yes +=1
        elif  choice == 'no':
            choice = 'no'
            no += 1
        else:
            print("That is not yes or no  answer but okay")

        result[name]= choice
        print(f"Thankyou !Your vote of {choice} has been recorded")

total_votes = len(result.keys())
print(f"The following {total_votes} people voted:")
for key in result.keys():
    print(key)

print(f"On the following issue: {issue}")
if yes >no:
    print(f"Yes wins! {yes} votes to {no}.")
elif no >yes:
    print(f"No wins! {no} votes to {yes}.")
else:
    print(f"It's a tie! {no} votes to {yes}")


guess = input("To see the voting result enter your the admin password")
if guess == password:
    for key,value in result.items():
        print(f"Voter {key}  \t\t\tVote: {value}")
else:
    print("You have enter the wrong result")

print("Thankyou for using Yes or No Polling App")