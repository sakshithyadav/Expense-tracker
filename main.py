from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    update_expense,
    delete_expense,
    expense_summary,
    search_expense
)

load_expenses()

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Expense Summary")
    print("6. Search Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        expense_summary()

    elif choice == "6":
        search_expense()

    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")