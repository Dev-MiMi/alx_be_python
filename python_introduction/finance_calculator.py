



monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
project_saving = (monthly_savings * 12.0 + (monthly_savings * 12.0 * 0.05))
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(project_saving)}.")
