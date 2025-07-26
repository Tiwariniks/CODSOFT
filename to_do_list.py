
def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append({'task': task, 'completed': False})
            print("Task added.")

        elif choice == '2':
            if not tasks:
                print("No tasks to display.")
            else:
                for i, task in enumerate(tasks):
                    status = "✔" if task['completed'] else "✗"
                    print(f"{i+1}. [{status}] {task['task']}")

        elif choice == '3':
            view_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= view_index < len(tasks):
                tasks[view_index]['completed'] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            delete_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= delete_index < len(tasks):
                removed = tasks.pop(delete_index)
                print(f"Removed task: {removed['task']}")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
