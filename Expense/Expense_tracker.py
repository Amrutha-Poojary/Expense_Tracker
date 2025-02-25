import json
from collections import defaultdict
from datetime import datetime

# Global list to store expenses
expenses = []

# Predefined categories
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

def add_expense():
    """
    Prompts the user to input expense details and adds the expense to the list.
    """
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter a brief description: ")
        category = input(f"Enter category ({', '.join(CATEGORIES)}): ").capitalize()
        if category not in CATEGORIES:
            print("Invalid category. Defaulting to 'Other'.")
            category = "Other"
        date = input("Enter date (YYYY-MM-DD): ")
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")
        
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

def view_expenses():
    """
    Displays all expenses in a readable format.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: ${expense['amount']:.2f} ({expense['description']})")

def analyze_expenses():
    """
    Analyzes expenses and provides monthly and category-wise summaries.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    monthly_total = defaultdict(float)
    category_total = defaultdict(float)

    for expense in expenses:
        month = expense["date"][:7]  # Extract year and month
        monthly_total[month] += expense["amount"]
        category_total[expense['category']] += expense["amount"]

    print("\nMonthly Totals:")
    for month, total in monthly_total.items():
        print(f"{month}: ${total:.2f}")

    print("\nCategory-wise Totals:")
    for category, total in category_total.items():
        print(f"{category}: ${total:.2f}")

def save_expenses():
    """
    Saves expenses to a JSON file.
    """
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    print("Expenses saved successfully!")

def load_expenses():
    """
    Loads expenses from a JSON file.
    """
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No existing data found. Starting with an empty list.")
    except json.JSONDecodeError:
        print("Error reading data. Starting with an empty list.")

def display_menu():
    """
    Displays the main menu for the Expense Tracker.
    """
    print("\nWELCOME TO THE EXPENSE TRACKER")
    print("\nExpense Tracker Menu:")
   
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Summary")
    print("4. View Category-wise Summary")
    print("5. Save Expenses")
    print("6. Exit")

def main():
    """
    Main function to run the Expense Tracker application.
    """
    load_expenses()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            analyze_expenses()  # Reuse the same function for category-wise summary
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()