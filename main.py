from task_manager import add_task, list_tasks, delete_task, count_tasks

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Count Tasks")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        add_task(title)

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    
    elif choice == "4":
        count_tasks()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")