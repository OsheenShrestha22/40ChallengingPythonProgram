print("--------------------------------------Power Ball Simulator-----------------------------------------")

#Determine the size of the lottery
#Get the number of the white-balls

white_balls = int(input("How many white-balls to draw from for the 5 winning number(Normally 69:)"))
if white_balls <5:
    white_balls=5

red_balls = int(input("How many red-balls to draw from the Power Ball(Normally 26:)"))
if red_balls <1:
    red_balls=1


#calculate the odds of winning this lottery

odds =1
for i in range(5):
    odds *=white_balls-i
odds *= red_balls/120

print(f"You have a 1 in {odds} chance of winning this lottery")
