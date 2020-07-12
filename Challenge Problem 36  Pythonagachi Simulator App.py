# Challenge Problem 36: Pythonagachi Simulator App
import random
# Define the Creature Class

class Creature():
    """Create a simple Tomagachi Clone."""
    def __init__(self,name):
        """Initialize attributes"""
        self.name =name

        # Attributies to track playing the game from (0-10)
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2#Represents Food Inventory
        self.is_sleeping = False #Bool to track if the creature is sleeping
        self.is_alive = True #Bool to track if the creature is alive



    def eat(self):
        """Simulate eating. Each time you eat, take one food away from the inventory and randomly take a value away from hunger"""
        if self.food > 0:
            self.food -= 1
            self.hunger -=random.randint(1,4)
            print(f"Yum! {self.name} ate a great meal!")
        else:
            print(f"{self.name} doesn't have any food! Better forage for some.")

        # If the hunger is less than zero set it to zero.

        if self.hunger< 0:
            self.hunger = 0

    def play(self):
        """Playing a guessing name to lower the creatures boredom
        If you win the game , lower the boredom even move"""
        # Simple guessing game
        value = random.randint(0,2)
        print(f"\n{self.name} wants to play the game.")
        print(f"{self.name} is thinking of a number 0,1 or 2")
        guess = int(input("What is your guess:"))

        if guess == value:
            print("That is correct!!!!!")
        else:
            print(f"Wrong!!! {self.name} was thinking of {value}.")
            self.boredom -=1

        if self.boredom < 0:
            self.boredom = 0


    def sleep(self):
        """Simulate the sleeping.The only thing that a player can do when the creature is sleeping is try to wake up.However the tiredness and boredom
        should decrease each round when sleep"""
        # Put the creature to sleep
        self.is_sleeping = True
        self.tiredness -=3
        self.boredom -=2
        print("Zzzzzzzzzzzzzz........Zzzzzzzzzzzzzz........Zzzzzzzzzzzzzz")

        # If tiredness and boredome is less than zero then set it to zero.

        if self.tiredness <0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0


    def awake(self):
        """Simulate randonly  waking a creature up."""
        # Creature has a 1/3 chance to randomly wake up
        value = random.randint(0,2)

        # If creature wakes up, set tiredness to zero!!

        if value == 0:
            print(f"{self.name} just woke up!!!")
            self.is_sleeping = False
            self.tiredness = 0

        else:
            print(f"{self.name} won't wake up...")
            self.sleep()

    def clean(self):
        """Simulate taking a bath to completely clean the creature."""
        self.dirtiness = 0
        print(f"{self.name} has taken a bath.All clean")


    def forage(self):
        """Simulate foraging for food.This will increase the creatures food attribute however it will also increase
        their dirtiness"""

        # Randomly find food from 0 to 4 pieces
        food_found = random.randint(0,4)
        self.food += food_found

        # Creatures get dirty from foraging
        self.dirtiness +=2

        print(f"{self.name} found {food_found} pieces of food!!")


    def show_value(self):
        print(f"\nCreature Name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredome (0-10): {self.boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")

        print(f"\nFood Inventory: {self.food} pieces")

        # Show Current Sleeping Status
        if self.is_sleeping:
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")


    def increment_values(self,diff):
        """User must set an arbitary difficulty.This will control how much damage you take each round.Update the current values of the creature based on the
        difficulty."""

        # Increase the hunger and dirtiness regardless if the  creature is  awake or sleeping.
        self.hunger += random.randint(0,diff)
        self.dirtiness += random.randint(0,diff)

        # If the creature is awake, he should be growing tired and growing bored.
        if self.is_sleeping == False:
            self.boredom += random.randint(0,diff)
            self.tiredness += random.randint(0, diff)


    def kill(self):
        """Check for all conditions to kill or sleep the creature"""
        # First two checks, will  kill the creature

        if self.hunger >= 10:
            print(f"{self.name} has starved to death." )
            self.is_alive == False

        elif self.tiredness >=10:
            print(f"{self.name} has suffered an infection and died..")

        # Next two checks, will put the creature to sleep.
        elif self.boredom >= 10:
            self.boredom =10
            print(f"{self.name} is bored. Falling asleep....")
            self.is_sleeping == True
        elif self.tiredness >=10:
            self.tiredness = 10
            print(f"{self.name} is sleepy.Falling asleep......")
            self.is_sleeping == True 


def show_menu(creature):

    """Show the menu options to the user.If the creature is sleeping, the player can only try to wake up the creature by default."""
    # If the creature is sleeping, only allow the user to wake the creature.
    # Hard code the value for the sneaky user.

    if creature.is_sleeping:
        choice = input("\nEnter 6 to try and wake up")
        choice = 6
    # Creature is awake, give full functionality to user
    else:
        print("\nEnter (1) to eat.")
        print("\Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take bath.")
        print("Enter (5) for forage for food.")
        choice = input("What is your choice:")

    return choice


def call_action(creature,choice):
    """Given the player choice, call the appropriate class method."""
    # Call the appropriate creature method

    if choice == '1':
        creature.eat()

    elif choice == '2':
        creature.play()

    elif choice == '3':
        creature.sleep()

    elif choice == '4':
        creature.bath()

    elif choice == '5':
        creature.forage()
    # User entered in invalid input. Do not call any methods
    else:
        print("Sorrr, that is not a valid move.")


# Set the difficulty level
difficulty = int(input("Please choose a difficulty level(1-5):"))

if difficulty > 5:
    difficulty = 5
elif difficulty <1:
    difficulty = 1

# The overall main game loop
running = True
while running:
    # Get the user input for creature name  and make a creature
    name = input("What name would you like to give to your pet Pythonagachi:")
    player =Creature(name)

    rounds =1
    # The game loop that simulates an individual round
    # This loop should run as long as the creature is alive
    while player.is_alive:
        print("\n-------------------------------------------------------------------------------------------------------------------")
        print(f"Round # {rounds}")
        player.show_value()
        round_move = show_menu(player)
        call_action(player,round_move)

        print(f"Round # {rounds} Summary:")

        # Summarize the effects of the current round
        player.show_value()
        input("\nPress enter to continue...........")

        #Increment values and check for death
        player.increment_values(difficulty)
        player.kill()

        #Round is over
        rounds +=1

    print("\nR.I.P")
    print(f"{player.name} survivided the total of {rounds-1} rounds")

    # Ask the user to play again
    choice = input("Would you like to play again (y/n):").lower()
    if choice != 'y':
        running = False
        print("Thankyou for playing Pythonagachi!!!!")




