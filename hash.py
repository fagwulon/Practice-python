def menu():
    display = """
    \n=======EXPENSE TRACKER=======
    \n1. Add Expense
    \n2. View Expense
    \n3. Calculate Total Expense
    \n4. Exit
    """
    print(display)
    option = input("Choose an option: ")

    while option not in ["1", "2", "3", "4"]:
        print("Invalid Option. Please enter 1, 2, 3 or 4")
        option = input("Choose an option: ")

    return option


def add_expense():
    item = input("Enter expense name: ")
    try:
        expense_amount = float(input(f"Enter cost for {item}: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value")
        expense_amount = 0.0

    expense_category = input("Enter expense category: ")

    return {"name": item, "amount": expense_amount, "category": expense_category}



def view_expense(add_expense):
    expense = add_expense
    print("\n======YOUR EXPENSE TRACKER======\n")
    for counter, item in enumerate(expense, start=1):

        return f"\n{counter}. {expense["name"]} - {expense['amount']} - {expense['category']}"


def calculate_total_expense(add_expense):
    expense = add_expense()
    total = 0
    for exp in expense:
        total += exp["amount"]
    return f"Total Expense: {total}"


def main():
    all_expense = []
    while True:
        option = menu()

        if option == "1":
            expense = add_expense()
            all_expense.append(expense)
        elif option == "2":
            view_expense(add_expense)
        elif option == "3":
            calculate_total_expense(add_expense)
        elif option == "4":
            break


main()
