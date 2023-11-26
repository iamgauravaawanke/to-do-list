tasks = {}

def add_task():
    task = input("Enter the task: ")
    priority = input("Enter priority (High, Medium, Low): ")
    tasks[task] = priority
    print("Task added!")

def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for task, priority in tasks.items():
            print(f"- {task} - Priority: {priority}")
    else:
        print("Your To-Do List is empty.")

def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        del tasks[task]
        print(f"'{task}' task removed.")
    else:
        print("Task not found in the list.")

while True:
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
