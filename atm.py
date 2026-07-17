balance = 1000

while True:
    print("\n =====ATM MENU=====")
    print("WELCOME")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(balance)
    elif choice == "2":
        print("Unavailable")
    elif choice == "3":
        print("Unavailable")
    elif choice == "4":
        print("Thank You For Using Our ATM")
        break
    else:
        print("Invalid Input! Try Again")
