import random
print("Welcome to the game of Rock, Paper,Scissors")

rounds = int(input("How many rounds would you like to play:"))
moves = ['rock','scissors','paper']
p_score =0
c_score=0

for round in (rounds):
    print(f"Round{round+1}")
    print(f"Player: {p_score}\t Computer: {c_score}")

    #Get the computer moves
    c_index = random.randint(0,2)
    c_choice = moves[c_index]

    # Get the player moves
    p_choice = str(input("Time to pick..rock,scissors,paper:")).lower().strip()

    #Valid guess
    if p_choice in moves:
        print(f"Computer : {c_choice}")
        print(f"Player:{p_choice}")
        # Computer chooses Rock

        if p_choice == 'rock' and c_choice == 'rock':
            winner = 'tie'
            phrase = "It's a tie how boring!"
        elif p_choice == 'scissors' and c_choice == 'rock':
            winner = 'computer'
            phrase = 'Rock Smashes Scissors'
        elif p_choice == 'paper' and c_choice == 'rock':
            winner = 'player'
            phrase = 'Paper covers rock!'

        # Computer chooses Paper

        elif p_choice == 'paper' and c_choice == 'paper':
            winner = 'tie'
            phrase = "It's a tie how boring!"
        elif p_choice == 'scissors' and c_choice == 'paper':
            winner = 'player'
            phrase = 'Scissors cut paper'
        elif p_choice == 'rock' and c_choice == 'paper':
            winner = 'computer'
            phrase = 'Paper covers rock!'

        # Computer chooses scissors

        elif p_choice == 'scissors' and c_choice == 'scissors':
            winner = 'tie'
            phrase = "It's a tie how boring!"
        elif p_choice == 'rock' and c_choice == 'scissors':
            winner = 'player'
            phrase = 'Rock Smashes Scissors'
        elif p_choice == 'paper' and c_choice == 'scissors':
            winner = 'computer'
            phrase = 'Scissor cut paper!'
        else:
            print("Round Winner not calculated")
            winner = 'tie'
            phrase = "It's a tie, how boring!"

        #Display Round Result
        print(f"\t {phrase}")
        if winner == 'player':
            print(f"You win round {round}")
            p_score +=1
        elif winner == 'computer':
            print(f"Computer win round {round}")
            c_score += 1
        else:
            print("This is a tie")

    #Player didnot made a valid move
    else:
        print("This is not a valid option!!!")
        print("Computer get the point")
        c_score += 1

print("\tFinal Game Results")
print(f"Rounds Played: {rounds}")
print(f"Player Score: {p_score}")
print(f"Computer Score: {c_score}")

if p_score > c_score:
    print("\tWinner:Player")
elif c_score > p_score:
    print("\tWinner:Computer")
else:
    print("\tThe game was a Tie")




