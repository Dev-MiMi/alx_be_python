



income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))
monthly_saving = income - total_expenses
project_saving = (monthly_saving * 12 + (monthly_saving * 12 * 0.05))
print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${int(project_saving)}.")
