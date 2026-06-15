import json

expenses = []


def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be positive.")
                continue

            break

        except ValueError:
            print("Enter a valid amount.")

    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses()

    print("Expense Added Successfully!")


def view_expenses():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\nID | Amount | Category | Description | Date")
    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['id']} | "
            f"{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['date']}"
        )


def update_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    try:
        expense_id = int(input("Enter Expense ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            amount = input(f"Amount ({expense['amount']}): ")
            category = input(f"Category ({expense['category']}): ")
            description = input(f"Description ({expense['description']}): ")
            date = input(f"Date ({expense['date']}): ")

            if amount:
                expense["amount"] = float(amount)

            if category:
                expense["category"] = category

            if description:
                expense["description"] = description

            if date:
                expense["date"] = date

            save_expenses()

            print("Expense Updated Successfully!")
            return

    print("Expense ID not found.")


def delete_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    try:
        expense_id = int(input("Enter Expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:
            expenses.remove(expense)

            save_expenses()

            print("Expense Deleted Successfully!")
            return

    print("Expense ID not found.")


def expense_summary():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    total = 0
    categories = {}

    for expense in expenses:

        amount = float(expense["amount"])
        total += amount

        category = expense["category"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n===== Expense Summary =====")

    print(f"\nTotal Spending: ₹{total}")

    print("\nCategory Wise Spending:")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")


def search_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    category = input("Enter category to search: ")

    found = False

    print("\nResults:")
    print("-" * 60)

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(
                f"{expense['id']} | "
                f"{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['description']} | "
                f"{expense['date']}"
            )

            found = True

    if not found:
        print("No matching expenses found.")
