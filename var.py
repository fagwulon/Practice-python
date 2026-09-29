def add_expense():
    """Prompts the user for expense details and returns a dictionary."""
    # 1. Ask the user for input
    item = input("Enter expense item name: ").strip()

    # 2. Safely get the cost as a float
    try:
        cost = float(input(f"Enter cost for '{item}': ₦"))
    except ValueError:
        print("❌ Invalid price. Setting cost to ₦0.00")
        cost = 0.0

    # 3. Return the data as a clean dictionary
    return {"item": item, "cost": cost}


# --- Main Program Loop ---
all_expenses = []  # A list to store all our expense dictionaries

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses & Exit")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        # Call the function and save the returned dictionary
        expense = add_expense()
        all_expenses.append(expense)
        print(f"✅ Added: {expense['item']} - ₦{expense['cost']:.2f}")

    elif choice == "2":
        print("\n--- Final Expense List ---")
        total = 0
        for exp in all_expenses:
            print(f"• {exp['item']}: ₦{exp['cost']:.2f}")
            total += exp['cost']

        print(f"\nTotal Spent: ₦{total:.2f}")
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please press 1 or 2.")
