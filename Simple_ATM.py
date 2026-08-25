# Displays the ATM menu and collects a valid option from the user

def func():
    display = """
    \n =====ATM=====
    \n1. Check Balance
    \n2. Deposit
    \n3. Withdraw
    \n4. Exit
    """
    print(display)
    option = input("Enter an option: ")

    # Keeps asking until user enters a valid menu option

    while option not in ('1', '2', '3', '4'):
        print("Invalid input. Enter 1, 2, 3 or 4.")
        option = input("Enter an option: ")

    return option


def check_balance(Balance):

    # Displays the user's current account balance

    print(f"Available Balance: ₦{Balance}")

    # Returns the balance so it can continue to be used by the program

    return Balance


# Handles deposits and updates the account balance

def deposit(Balance):
    amount = int(input("Enter Amount: "))

    # Prevents deposits below the minimum allowed amount

    if amount < 1000:
        print("Invalid Amount. Amount must be 1000 or more.")
    else:
        Balance += amount
        print(f"Successfully deposited ₦{amount: }")

    return Balance


# Handles withdrawals and updates the account balance

def withdraw(Balance):
    amount = int(input("Enter Amount: "))

    # Prevents zero or negative withdrawals

    if amount <= 0:
        print("Invalid Amount")

    # Prevents the user from withdrawing more than their balance

    elif amount > Balance:
        print("Insufficient funds!")
    else:
        Balance -= amount
        print(f"Successfully withdrew ₦{amount: }")
    return Balance


# Controls the main ATM program

def output():

    # Set the starting account balance

    Balance = 50000

    # Keep the ATM running until the user chooses Exit

    while True:
        option = func()

        # Display the current

        if option == '1':
            Balance = check_balance(Balance)

        # Process a deposit

        elif option == '2':
            Balance = deposit(Balance)

        # Process a withdrawal

        elif option == '3':
            Balance = withdraw(Balance)

        # Exit the ATM

        elif option == '4':
            print("\nThanks for using the ATM. Goodbye!")
            break


# Start the ATM program
output()
