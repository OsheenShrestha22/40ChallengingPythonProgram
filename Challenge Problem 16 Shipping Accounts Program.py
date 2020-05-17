print("Welcome to the Shipping Accounts Program")
user_name = ['raman','osheen','mona']

name = str(input("\nWhat is your username:"))
if name in user_name:
    print(f"Hello! {name}.Welcome back to your account.")
    print("\nCurrent shipping prices are as follows:\n")
    print("Shipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    items = int(input("\nHow many items would you like to ship:"))
    if items < 100:
       cost =5.10
    elif items < 500:
        cost =5.00
    elif items < 1000:
        cost =4.95
    else:
        cost =4.80
    bill = cost*items
    bill = round(bill,2)
    print(f"To ship {items} it will cost you $ {bill}")

    place_order = str(input("\nWould you like to place this order (y/n):"))

    if place_order == 'y':
        print("Your order will be placed ")
    else:
        print("Okay no order will be placed this time")
else:
    print("Sorry, you dont  have an account with us. Good Bye!")




