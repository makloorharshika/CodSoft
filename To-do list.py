import os

# File to store tasks
FILE_NAME = "todo_list.txt"

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

# Function to update an existing task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_number - 1] = new_task
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
