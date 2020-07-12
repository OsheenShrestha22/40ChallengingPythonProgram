print('Welcome to the Database Admin Program')

information = {
     'admin':'ilovemyself',
    'osheen':'iloveu',
    'pramod':'ilovemybudi',
    'anajana':'ilovemybud',
}

username = str(input('Enter your username:'))
if username in information.keys():
    user_password = str(input('Enter your password:'))
    if user_password == information[username]:
        print(f'Hello {username}! You are logged in!')
        if username == 'admin':
            print('Here is the list of the database:')
            for key,value in information.items():
                print(f"Username: {key} \t\tPassword: {value}")
        else:
            choice =str(input("Would you like to change your password yes/no:")).lower()
            if choice == 'yes':
                new_password =str(input("What would you like your new password to be:"))
                if len(new_password) >= 8:
                    information[username] = new_password
                else:
                    print(f"{new_password} is not minimum eight character")
                print(f"{username} your new password is {user_password}")
            else:
                print('Thankyou,goodbye!')

    else:
         print('incorrect password')
else:
    print('Username not in database,goodbye')