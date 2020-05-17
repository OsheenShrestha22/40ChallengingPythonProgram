print("Welcome to the Favorite Teachers Program")

teacher_list = []
teacher_list.append(input("Who is your first favorite teacher:"))
teacher_list.append(input("Who is your second favorite teacher:"))
teacher_list.append(input("Who is your third favorite teacher:"))
teacher_list.append(input("Who is your fourth favorite teacher:"))

print(f"\nYour favorite teachers ranked are: {teacher_list}")
teacher_list.sort()
print(f"Your favorite teachers alphabetically are: {teacher_list}")
teacher_list.sort(reverse=False)
print(f"Your favorite teachers in reverse alphabetical order are: {teacher_list}")
print(f"Your top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your remaining teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"Your last favorite teacher is:{teacher_list[3]}")
print(f"You have a total of {len(teacher_list)} favorite teachers")

print(f"\nOpps!! {teacher_list[0]} is no longer your favorite teacher.Who is your fav teacher:",end='')
teacher_list.pop(0)
teacher_list.append(input())


print(f"Your favorite teachers ranked are: {teacher_list}")
teacher_list.sort()
print(f"Your favorite teachers alphabetically are: {teacher_list}")
teacher_list.sort(reverse=False)
print(f"Your favorite teachers in reverse alphabetical order are: {teacher_list}")
print(f"Your top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your top two teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"Your last favorite teacher is:{teacher_list[3]}")
print(f"You have a total of {len(teacher_list)} favorite teachers")


not_fav = input("You have decide you no longer like a teacher.Which teacher would you like to remove from your list:")
teacher_list.remove(not_fav)

print(f"Your favorite teachers ranked are: {teacher_list}")
teacher_list.sort()
print(f"Your favorite teachers alphabetically are: {teacher_list}")
teacher_list.sort(reverse=False)
print(f"Your favorite teachers in reverse alphabetical order are: {teacher_list}")
print(f"Your top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your top two teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"Your last favorite teacher is:{teacher_list[3]}")
print(f"You have a total of {len(teacher_list)} favorite teachers")