def menu():
    display = """
    \n=====ATM=====
    \n1. Check Balance
    \n2. Deposit
    \n3. Withdraw
    \n4. Exit
    """
    print(display)

    option = input("Enter an option: ")

    while option not in ('1', '2', '3', '4'):
        print("Invalid input. Please enter 1, 2, 3 or 4.")
        option = input("Enter an option: ")

    return option


def check_balance(Balance):
    print(f"\nAvailable Balance: ₦{Balance}")

    return Balance


def deposit(Balance):
    amount = float(input("Enter Amount: "))

    if amount < 1000:
        print("Invalid Amount. Amount must be 1000 or more.")
    else:
        Balance += amount
        print(f"\nSuccessfully deposited ₦{amount}")

    return Balance


def withdraw(Balance):
    amount = float(input("Enter Amount: "))

    if amount <= 0:
        print("Invalid Amount!")
    elif amount > Balance:
        print("Insufficient funds!")
    else:
        Balance -= amount
        print(f"\nSuccessfully withdrew ₦{amount}")

    return Balance


def output():
    Balance = 50000

    while True:
        option = menu()

        if option == '1':
            Balance = check_balance(Balance)

        elif option == '2':
            Balance = deposit(Balance)

        elif option == '3':
            Balance = withdraw(Balance)

        elif option == '4':
            print("\nThanks for using the ATM. Goodbye!\n")
            break


# Start the ATM program
output()
