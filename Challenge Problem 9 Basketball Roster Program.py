print("Welcome to the Basketball Roster Program")

players =[]

players.append(input("Who is your point guard:"))
players.append(input("Who is your shooting guard:"))
players.append(input("Who is your small guard:"))
players.append(input("Who is your power forward:"))
players.append(input("Who is your center:"))
print(players)

print("\n\tYour starting 5 for you upcoming basketball season")
print("\t\tpoint guard\t\t" + players[0])
print("\t\tshooting guard\t\t" + players[1])
print("\t\tsmall guard\t\t\t" + players[2])
print("\t\tpower forward\t\t" + players[3])
print("\t\tcenter\t\t\t\t" + players[4])

injured_player =   players.pop(2)
print(f"Oh! No {injured_player} is injured!!")
print(f"Your roster only have {len(players)} players.")

add_player = input(f"Who will you take {injured_player} 's spot:")
players.insert(2,add_player)


print("\n\tYour starting 5 for you upcoming basketball season")
print("\t\tpoint guard\t\t\t" + players[0])
print("\t\tshooting guard\t\t" + players[1])
print("\t\tsmall guard\t\t\t" + players[2])
print("\t\tpower forward\t\t" + players[3])
print("\t\tcenter\t\t\t\t" + players[4])


print(f"Good Luck {add_player} you will do great!!!")
print(f"Your roster has {len(players)}")