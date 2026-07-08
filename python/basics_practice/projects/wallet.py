# ===== Expense Tracker =====

menu_price = []


def show_expense():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Show Total Expenses")
    print("6. Exit")


def add_expense():
    try:
        add_name = input("Enter name: ")
        add_category = input("Enter category: ")
        add_price = int(input("Enter price: "))

        menu_price.append({
            "name": add_name,
            "category": add_category,
            "price": add_price
        })

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_expense():
    if not menu_price:
        print("No expenses found.")
        return

    print("\n===== Expenses =====")

    for index, expense in enumerate(menu_price, start=1):
        print(f"{index}.")
        print(f"Name     : {expense['name']}")
        print(f"Category : {expense['category']}")
        print(f"Price    : {expense['price']}")
        print("-" * 25)


def serch_expense():
    if not menu_price:
        print("No expenses found.")
        return

    search = input("Enter expense name: ")

    for item in menu_price:
        if search == item["name"]:
            print("\nExpense Found")
            print(f"Name     : {item['name']}")
            print(f"Category : {item['category']}")
            print(f"Price    : {item['price']}")
            return

    print("Expense not found.")


def delete_expense():
    if not menu_price:
        print("No expenses found.")
        return

    delete = input("Enter expense name to delete: ")

    for index, item in enumerate(menu_price):
        if delete == item["name"]:
            removed = menu_price.pop(index)
            print(f"{removed['name']} deleted successfully!")
            return

    print("Expense not found.")


def total_expense():
    if not menu_price:
        print("No expenses found.")
        return

    total = 0

    for item in menu_price:
        total += item["price"]

    print(f"Total Expenses: {total}")


def main():
    while True:
        show_expense()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expense()

        elif choice == "3":
            serch_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            total_expense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()