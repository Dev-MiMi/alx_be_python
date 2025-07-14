
task_des = input("Enter your task: ").capitalize()
level = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match level:
    case "high":
        if time == "yes":
            print(f"Reminder: {task_des} is a {level} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: {task_des} is a {level} priority task. Consider completing it when you have free time.")
    case "medium":
        if time == "yes":
            print(f"Reminder: {task_des} is a {level} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: {task_des} is a {level} priority task. Consider completing it when you have free time.")
    case "low":
        if time == "yes":
            print(f"Reminder: {task_des} is a {level} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: {task_des} is a {level} priority task. Consider completing it when you have free time.")

