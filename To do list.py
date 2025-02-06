# Function to display the menu
def display_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Edit Task")
    print("4. Display Tasks")
    print("5. Mark Task as Completed")
    print("6. Exit")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nNo tasks to display.")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to edit: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num - 1] = new_task
            print(f"Task updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1] + " - Completed"
            print(f"Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to save tasks to a file
def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to file.")

# Function to load tasks from a file
def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

# Main function to run the app
def run_app():
    tasks = load_tasks_from_file()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            mark_completed(tasks)
        elif choice == '6':
            save_tasks_to_file(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_app()
