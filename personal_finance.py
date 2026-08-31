monthly_income = int(input("Enter monthly income: "))

rent = int(input("Expense on rent: "))
food =  int(input("Expense on food: "))
transport = int(input("Expense on transport: "))
other_expenses = int(input("Other expenses: "))

total_expenses = rent + food + transport + other_expenses

remaining_money = monthly_income - total_expenses

expense_percentage = (total_expenses / monthly_income) * 100 / 1

balance_percentage = (remaining_money / monthly_income) * 100 / 1


print(f"\nMonthly income: {monthly_income}\n")
print(f"\nYour total expense for the month: {total_expenses}")
print(f"\nExpense percentage: {expense_percentage}\n")
print(f"\nBalance after expenses: {remaining_money}%")
print(f"\nBalance percentage: {balance_percentage}%\n")