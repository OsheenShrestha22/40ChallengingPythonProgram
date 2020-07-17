```ruby
print("Welcome to the letter Counter App")
name = input("Please enter your name :").title().strip()
print(f"Hello {name}!")
print('I will count the number of times that a specific letter occurs in a message')
message = input("Please enter a message")
print("Which leter would you like to count the occurance of:")
character = str(input())
message = message.lower()
character = character.lower()
"""
This is one way
count = 0
for i in message:
    if i == character:
        count += 1
print(count)
"""

letter_count = message.count(character)
```ruby
