# created an to-do2

tasks = []

def show_menu():
    print("---to-do-list---")
    print("1. add task")
    print("2. view_task")
    print("3. mark task as done")
    print("4. delete task")
    print("5. Exept")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task":task, "done":False})
    print(f"task{task} added!")

def view_task():
    if not tasks:
        print("no task yet!")
        return
    print("\nyour task")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task} [{status}] ")

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done!")) -1
        if index < 0 or index >= len(tasks):
            print("invallid number")
        else:
            tasks[index]["done"] = True
    except ValueError:
        print("pleas enter avallid number")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete")) -1
        if index < 0 or index >= len(tasks):
            print("vallid number")
        else:
            removed = tasks.pop(index)
            print(f"{removed['task']} delete sucssfully")
    except ValueError:
        print("vallid number")

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
        break
    else:
        print("invalid choice. try again.")
    