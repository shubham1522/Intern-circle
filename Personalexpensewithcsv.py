import csv
import os

FILENAME = "expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Enter description: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            print("\n=== All Expenses ===")
            for row in reader:
                print("{:<12} {:<15} {:<10} {}".format(*row))

    except FileNotFoundError:
        print("No expense records found.")


def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()

    found = False

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nFiltered Results:")
        for row in reader:
            if row["Category"].lower() == category:
                print(
                    f"{row['Date']} | "
                    f"{row['Category']} | "
                    f"₹{row['Amount']} | "
                    f"{row['Description']}"
                )
                found = True

    if not found:
        print("No matching expenses found.")


def category_summary():
    summary = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    print("\n=== Category Summary ===")

    total = 0

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")
        total += amount

    print(f"\nTotal Expenses: ₹{total:.2f}")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()