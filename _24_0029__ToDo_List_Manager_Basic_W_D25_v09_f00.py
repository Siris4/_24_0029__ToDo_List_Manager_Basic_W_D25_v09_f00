def add_task(task_list):
    task = input("Enter a task: ")
    task_list.insert(0, task)  # Inserts the new task at the beginning of the list
    print("Task added to the top of the list.\n")


def view_tasks(task_list):
    if task_list:
        print("To-Do List:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.\n")


def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        task_num = int(input("\nEnter the task number to delete: "))
        if 0 < task_num <= len(task_list):
            del task_list[task_num - 1]
            print("Task deleted.\n")
        else:
            print("Invalid task number.\n")


def main():
    task_list = []

    while True:
        print("A. Add a Task")
        print("B. View Tasks")
        print("C. Delete a Task")
        print("D. Exit")

        choice = input("\nEnter your choice: ")

        if choice == 'A' or choice == 'a':
            add_task(task_list)
        elif choice == 'B' or choice == 'b':
            view_tasks(task_list)
        elif choice == 'C' or choice == 'c':
            delete_task(task_list)
        elif choice == 'D' or choice == 'd':
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
