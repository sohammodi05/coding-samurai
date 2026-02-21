# Command-line To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        show_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
