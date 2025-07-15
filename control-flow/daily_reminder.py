task_des = input("Enter your task: ")
level = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match level:
    case "high" | "medium" | "low":
        task_des = task_des[0].upper() + task_des[1:]  # Capitalize task
        message = ""

        if time == "yes":
            message = f"Reminder: '{task_des}' is a {level} priority task that requires immediate attention today!"
            for i in range(3):  # loop to reinforce urgency
                print(message)
        elif time == "no":
            message = f"Note: '{task_des}' is a {level} priority task. Consider completing it when you have free time."
            print(message)
        else:
            print("Invalid time-bound input. Please enter 'yes' or 'no'.")
    case _:
        print("Invalid priority level entered.")
