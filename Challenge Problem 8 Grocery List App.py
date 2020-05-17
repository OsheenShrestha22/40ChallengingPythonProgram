from datetime import datetime
print("Welcome to the Grocery List App.")
now = datetime.now()
dt_string = now.strftime("%d/%m %H:%M")
print("Current Date and Time =", dt_string)
list=['meat','cheese']
print("You Current have Meat and Cheese in your list\n")

list.append(input("Type of food to add to the grocery list:"))
list.append(input("Type of food to add to the grocery list:"))
list.append(input("Type of food to add to the grocery list:"))


print(f"\nHere is your grocery list: {list}")
list.sort()
print(f"Here is your grocery list sorted:{list}")

print("\nSimulating grocery shopping...\n")

print(f"Current grocery list:{len(list)}")
print(list)
buy_food =(input("What food did you buy:"))
list.remove(buy_food)
print(" Removing"+ str(buy_food) + "from list.....\n")

print(f"Current grocery list:{len(list)}")
print(list)
buy_food =(input("What food did you buy:"))
list.remove(buy_food)
print(" Removing"+ str(buy_food) + "from list.....\n")

print(f"Current grocery list:{len(list)}")
print(list)
buy_food =(input("What food did you buy:"))
list.remove(buy_food)
print(" Removing"+ str(buy_food) + "from list.....\n")

if len(list) == 2:
    print(f"Sorry the store is out of {list[0]}\n")

list.pop(0)

list.append(input("What food would you like instead:"))
print("Here is what remains in your grocery lists:")
print(list)