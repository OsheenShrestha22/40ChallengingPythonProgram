import random
print("Welcome to the Guess My Number App")

name= str(input("\nHello!What is your name:"))
print(f"Well {name},I am thinking of a bewtween 1 and 20")
correct_num = random.randint(1,21)

for guess_num in range(5):
    guess = int(input("Take a guess:"))

    if guess > correct_num:
        print("Your guess to high")

    elif guess < correct_num:
        print("Your guess is to low")

    else:
        break

if guess == correct_num:
    print(f"Good Job {name}!! You guessed my number in {guess_num+1} guess.")
else:
    print(f"Game Over the number is was thinking of is {correct_num}")
