# To-Do List CLI App

tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)

# Function to remove a task
def remove_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Task removed:", removed)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main menu
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
