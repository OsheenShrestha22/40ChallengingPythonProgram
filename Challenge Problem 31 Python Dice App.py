import random


def dice_sides():
    """Ask users how many sides would you like in their dice"""
    sides = int(input("\nHow many side would you like on your dice:"))
    return sides


def dice_number():
    """Ask the user how many dice to roll"""
    number = int(input("How many dice would you like to roll:"))
    return number


def roll_dice(sides, number):
    """Simulate rolling the dice"""
    dice = []
    print(f"you rolled {number} {sides} sided dice.")
    print("\n-----------Results are as followed-------------")

    for i in range(number):
        value = random.randint(1, sides)
        print(f"\t{value}")
        dice.append(value)
    return dice


def sum_dice(dice):
    """Add all the values of a dice in a list"""
    total = 0
    for die in dice:
        total += die
    print(f"The total value of your roll is {total}")


def roll_again():
    choice = input("Would you like to run the program again (y/n):").lower()
    if choice != 'y':
        roll = False
    else:
        roll = True
    return roll

print("Welcom to Python Dice App")

rolling = True
while rolling:
    #Get the information for the type of the dice
    d_side =dice_sides()
    d_number =dice_number()

    my_side = roll_dice(d_side,d_number)
    sum_dice(my_side)

    rolling = roll_again()

print("Thankyou For Using Python Dice App")



