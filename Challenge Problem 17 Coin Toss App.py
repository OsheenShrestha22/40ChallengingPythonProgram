import random

print("Welcome to the Coin Toss App:")

print("\nI will flip a coin a set of number of times:")
num = int(input("How many time would you like to flip the coins:"))
ans = str(input("Would you like to see the result of each flip: (y/n)")).lower()

head = 0
tail = 0

for coin in range(num):
    coin = random.randint(0, 1)

    if coin == 1:
        head += 1
        if ans.startswith('y'):
            print('HEADS')
    else:
        tail += 1
        if ans.startswith('y'):
            print('TAILS')

    if head == tail:
        print(f"At {coin + 1} flips, the number of heads and tails were equal at {head} each.")

# Calculate the percentages
head_percentage = round(100 * head / num, 2)
tail_percentage = round(100 * tail / num, 2)

# Print the results

print(f"\nResults of Flipping a coin {num} times")
print("\nSide\t\tCount\t\Percentage")
print(f"Heads\t\t{head}/{num}\t\t{head_percentage}%")
print(f"Heads\t\t{tail}/{num}\t\t{tail_percentage}%")
