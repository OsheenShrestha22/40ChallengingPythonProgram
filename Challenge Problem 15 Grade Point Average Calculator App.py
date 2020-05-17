print("Welcome to the Average Calculator App")

name = str(input("What is your name:"))
grade_count=int(input("How many grades would you like to enter:"))


grades = []
for i in range(grade_count):
    grades.append(int(input("Enter grade:")))

print("Grades Highest to Lowest:")
grades.sort(reverse= True)

for number in grades:
    print(f"\t{number}")

print(f"{name}'s Grade Summary:")

print(f"Total Number of Grades: {grade_count}")
print(f"Highest Grade:{grades[0]}")
print(f"Lowest Grade:{grades[-1]}")
average = sum(grades)/len(grades)
print(f"Average Grade:{average}")

desire_ave =float(input("What is your desired average:"))
grades_required = desire_ave*(len(grades)+1) -sum(grades)
grades_required = round(grades_required,2)
print(f"Good Luck {name}!")
print(f"You will need to get a {grades_required} on your next assignment to earn a {desire_ave}")


print("Let's see what your average could have been if you did better/worse on an assignment:")


new_grade = grades[:]
print(new_grade)
grade_changed = int(input("What grade would you like to change: "))
new_grade.remove(grade_changed)
grade_changed = int(input(f"What grade would you like to change {grade_changed} to:"))
new_grade.append(grade_changed)


print("Grades Highest to Lowest:")
new_grade.sort(reverse= True)

for number in new_grade:
    print(f"\t{number}")

print(f"{name}'s Grade Summary:")

print(f"Total Number of Grades: {grade_count}")
print(f"Highest Grade:{new_grade[0]}")
print(f"Lowest Grade:{new_grade[-1]}")
new_average = sum(new_grade)/len(new_grade)
print(f"Average Grade:{new_average}")

print(f"Your new average would be {new_average} compared to your real average of {average}")
change = new_average - average
print(f"That is a change of {change}points!")

print("Too bad your original grades are still the same!!")
print(grades)
print("You should as for extra credit")


