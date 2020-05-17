print("Welcome to the Grade Sorter App")

grade = []

grade.append(input("What is your first grade(0-100):"))
grade.append(input("What is your second grade(0-100):"))
grade.append(input("What is your third grade(0-100):"))
grade.append(input("What is your fourth grade(0-100):"))
print(f"Your grades are:{grade}")
grade.sort(reverse = True)
print(f"Your reversed grades are:{grade}")

print("The lowest two grades will now be dropped.")
remove_grades =grade.pop()
print(f"Remove grades:{remove_grades}")
remove_grades =grade.pop()
print(f"Remove grades:{remove_grades}")

print(f"Your remaining grades are:{grade}")
print(f"Nice Work! Your highest grades is:" + grade[0])