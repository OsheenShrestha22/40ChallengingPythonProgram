import random
print("Welcome to the Guess My Word App")

game_dic = {
    "sport":['basketball','football','soccer','tennis','badminton'],
    "colors":['red','green','blue','white','black'],
    "fruits":['orange','apple','banana','grapes','mango','cherry'],
    "classes":['english','history','science','math','bio','nepali'],
}

#Create a list of keys

game_keys =[]

for key in game_dic.keys():
    game_keys.append(key)


#The main game loop

playing = True
while playing:
    #Randomly pick the game category and the game word from the data dictionary
    game_category = game_keys[random.randint(0,len(game_keys)-1)]
    game_word = game_dic[game_category][random.randint(0,len(game_dic[game_category])-1)]

    #Build a dashed "-" word to represent the game word
    blank= []
    for letter in game_word:
        blank.append('-')

    print(f"Guess a {len(game_word)} letter word from the following category {game_category}")

    guess =""
    guess_count = 0
    #A single round loop

    while guess !=game_word:
        print("".join(blank))
        #Get the single guess from the user
        guess = input("Enter your guess.").lower()
        guess_count +=1

        #Guess is correct, user won the game

        if guess == game_word:
            print(f"\nCorrect! You guess the word in {guess_count} guesses.")
            break

        else:
            print("That is not correct.Let us reveal a letter to help you.")
            swapping = True
            while swapping:
                letter_index = random.randint(0,len(game_word)-1)
                if blank[letter_index] == "-":
                    blank[letter_index] = game_word[letter_index]
                    swapping = False

    choice = input("Would you like to run the program again (y/n):").lower()
    if choice != 'y':
        running = False
        print("Thankyou for using the program! GoodBye!")