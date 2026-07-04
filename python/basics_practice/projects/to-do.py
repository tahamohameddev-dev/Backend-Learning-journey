# Creating a To-Do List

tasks = []

def show_menu():
    print("\n--- to-do list ---")
    print("1. add task")
    print("2. view task")
    print("3. mark task as done!")
    print("4. delete task")
    print("5. exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task":task, "done":False})
    print(f"Task'{task}' added!")

def view_task():
    if not tasks:
        print("no tasks yet!")
        return
    print("\nYour task:  ")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task["task"]} [{status}]")

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("enter task nomber to mark done: ")) -1
        if index < 0 or index >= len(tasks):
            print("invalid number")
        else:
            tasks[index]["done"] = True
    except ValueError:
        print("please enter a valid number. ")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("enter task number to delet: ")) -1
        if index < 0 or index >= 0:
            print("envalid number")
        else:
            removed = tasks.pop(index)
            print(f"task {removed['task']} delete sucssfully")
    except ValueError:
        print("pleas enter a valid number.")

while True:
    show_menu()
    choice = input("Enter an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("goodby")
    else:
        print("invalid choice. try again.")
