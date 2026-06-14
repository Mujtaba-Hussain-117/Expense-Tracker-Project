"""
Expense Tracker - Python Project
Tools: Python, File Handling (CSV)
Features: Add expenses, view all, category summary, filter by date/category
"""

import os
print("Saving data to:", os.path.abspath("expenses.csv"))
import csv
import os
from datetime import datetime


# ──────────────────────────────────────────────
#  CONFIG
# ──────────────────────────────────────────────
DATA_FILE = "expenses.csv"
FIELDNAMES = ["id", "date", "category", "description", "amount"]

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Health",
    "Bills",
    "Education",
    "Other",
]


# ──────────────────────────────────────────────
#  FILE HELPERS
# ──────────────────────────────────────────────
def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        print(f"  [Created new data file: {DATA_FILE}]")


def load_expenses():
    """Read all expenses from the CSV file."""
    expenses = []
    with open(DATA_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    """Overwrite the CSV file with the given list of expenses."""
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def next_id(expenses):
    """Return the next auto-increment ID."""
    if not expenses:
        return 1
    return max(int(e["id"]) for e in expenses) + 1


# ──────────────────────────────────────────────
#  CORE OPERATIONS
# ──────────────────────────────────────────────
def add_expense():
    """Prompt the user and save a new expense."""
    print("\n── Add New Expense ──────────────────────────")

    # Date
    date_input = input("  Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date_input:
        date_input = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("  ✗ Invalid date format. Expense not added.")
            return

    # Category
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    cat_choice = input("  Choose category number: ").strip()
    if not cat_choice.isdigit() or not (1 <= int(cat_choice) <= len(CATEGORIES)):
        print("  ✗ Invalid choice. Expense not added.")
        return
    category = CATEGORIES[int(cat_choice) - 1]

    # Description
    description = input("  Description: ").strip()
    if not description:
        print("  ✗ Description cannot be empty.")
        return

    # Amount
    amount_input = input("  Amount (PKR): ").strip()
    try:
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("  ✗ Invalid amount. Please enter a positive number.")
        return

    # Save
    expenses = load_expenses()
    expense = {
        "id": next_id(expenses),
        "date": date_input,
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\n  ✓ Expense added! [ID: {expense['id']}]  PKR {amount:,.2f} for {description}")


def view_all_expenses():
    """Display every expense in a formatted table."""
    expenses = load_expenses()
    print("\n── All Expenses ─────────────────────────────")
    if not expenses:
        print("  No expenses recorded yet.")
        return

    # Table header
    print(f"  {'ID':<5} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount (PKR)':>12}")
    print("  " + "─" * 72)

    total = 0.0
    for e in expenses:
        print(
            f"  {e['id']:<5} {e['date']:<12} {e['category']:<15} "
            f"{e['description']:<25} {e['amount']:>12,.2f}"
        )
        total += e["amount"]

    print("  " + "─" * 72)
    print(f"  {'TOTAL':<53} {total:>12,.2f}")
    print(f"  ({len(expenses)} record(s))")


def summary_by_category():
    """Show total spending grouped by category."""
    expenses = load_expenses()
    print("\n── Summary by Category ──────────────────────")
    if not expenses:
        print("  No expenses recorded yet.")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    grand_total = sum(totals.values())

    print(f"  {'Category':<20} {'Total (PKR)':>12}  {'Share':>7}")
    print("  " + "─" * 44)
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        share = (amt / grand_total * 100) if grand_total else 0
        bar = "█" * int(share / 5)   # simple bar chart (each block ≈ 5%)
        print(f"  {cat:<20} {amt:>12,.2f}  {share:>6.1f}%  {bar}")

    print("  " + "─" * 44)
    print(f"  {'GRAND TOTAL':<20} {grand_total:>12,.2f}")


def filter_by_month():
    """Show expenses for a specific month."""
    month_input = input("\n  Enter month (YYYY-MM): ").strip()
    try:
        datetime.strptime(month_input, "%Y-%m")
    except ValueError:
        print("  ✗ Invalid format. Use YYYY-MM.")
        return

    expenses = load_expenses()
    filtered = [e for e in expenses if e["date"].startswith(month_input)]

    print(f"\n── Expenses for {month_input} ─────────────────────────")
    if not filtered:
        print("  No expenses found for that month.")
        return

    total = 0.0
    print(f"  {'ID':<5} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>12}")
    print("  " + "─" * 72)
    for e in filtered:
        print(
            f"  {e['id']:<5} {e['date']:<12} {e['category']:<15} "
            f"{e['description']:<25} {e['amount']:>12,.2f}"
        )
        total += e["amount"]
    print("  " + "─" * 72)
    print(f"  {'TOTAL':<53} {total:>12,.2f}")


def delete_expense():
    """Delete an expense by its ID."""
    view_all_expenses()
    id_input = input("\n  Enter the ID to delete (or 0 to cancel): ").strip()
    if id_input == "0":
        return

    expenses = load_expenses()
    new_expenses = [e for e in expenses if str(e["id"]) != id_input]

    if len(new_expenses) == len(expenses):
        print("  ✗ ID not found.")
        return

    save_expenses(new_expenses)
    print(f"  ✓ Expense ID {id_input} deleted.")


# ──────────────────────────────────────────────
#  MAIN MENU
# ──────────────────────────────────────────────
def main():
    initialize_file()
    print("╔══════════════════════════════════════╗")
    print("║        EXPENSE TRACKER  💰            ║")
    print("╚══════════════════════════════════════╝")

    menu = {
        "1": ("Add Expense",            add_expense),
        "2": ("View All Expenses",      view_all_expenses),
        "3": ("Summary by Category",    summary_by_category),
        "4": ("Filter by Month",        filter_by_month),
        "5": ("Delete an Expense",      delete_expense),
        "0": ("Exit",                   None),
    }

    while True:
        print("\n── Menu ─────────────────────────────────")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\n  Choose an option: ").strip()

        if choice == "0":
            print("\n  Goodbye! Stay on budget 👋\n")
            break
        elif choice in menu:
            _, action = menu[choice]
            action()
        else:
            print("  ✗ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
