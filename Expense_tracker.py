def menu():
    display = """
    \n======EXPENSE TRACKER======
    \n1. Add Expense
    \n2. View Expense
    \n3. Calculate total
    \n4. Exit
    """
    print(display)

    option = input("Enter your choice: ")

    while not option in ("1", "2", "3", "4"):
        print("Invalid choice. \nEnter 1, 2, 3, or 4")
        option = input("Enter your choice: ")

    return option


def add_expense():
    Expense_name = input("Enter Expense Name: ")

    while True:
        try:
            Expense = float(input("Enter Expense Amount: "))
            break
        except ValueError:
            print("Invalid Expense amount!\nPlease enter a numeric value.\n")

    Expense_category = input("Enter Expense Category: ")

    return {"Name": Expense_name, "Amount": Expense, "Category": Expense_category}


def view_expenses(expenses):
    if not expenses:
        print("\nNo expense recorded yet.")
        return
    print("\n======YOUR EXPENSES======\n")
    for count, expense in enumerate(expenses, start=1):
        print(
            f"{count}. {expense['Name']} - {expense['Amount']:.2f} - {expense['Category']}")


def calculate_total(expenses):
    total = sum(expense['Amount'] for expense in expenses)
    return f"\nTotal Expense: ${total:.2f}"


def main():
    all_expenses = []

    while True:
        option = menu()

        if option == '1':
            expenses = add_expense()
            all_expenses.append(expenses)
            print(f"Added {expenses['Name']} successfully!")
        elif option == '2':
            view_expenses(all_expenses)
        elif option == '3':
            print(calculate_total(all_expenses))
        elif option == '4':
            print("Goodbye!")
            break


main()
