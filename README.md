# Expense-Tracker-Project


💰 Expense Tracker

A command-line expense tracking application built with pure Python and CSV file handling — no external libraries required.


📋 Table of Contents


Features
Requirements
How to Run
How to Use
Project Structure
Data Storage
Categories
Python Concepts Covered
Example Output



✨ Features

FeatureDescription➕ Add ExpenseLog date, category, description, and amount📄 View AllDisplay every expense in a formatted table with total📊 SummaryTotals grouped by category with a visual bar chart🗓️ Filter by MonthShow only expenses from a specific month🗑️ DeleteRemove any expense by its ID💾 Persistent StorageAll data saved to a CSV file automatically


⚙️ Requirements


Python 3.6 or higher
No external libraries needed — uses only Python's built-in modules:

csv
os
datetime






▶️ How to Run


Download expense_tracker.py to your computer.
Open a terminal in the same folder.
Run the script:


bashpython expense_tracker.py


On some systems, use python3 instead of python.




🖥️ How to Use

When you run the program, you'll see the main menu:

╔══════════════════════════════════════╗
║        EXPENSE TRACKER  💰            ║
╚══════════════════════════════════════╝

── Menu ─────────────────────────────────
  1. Add Expense
  2. View All Expenses
  3. Summary by Category
  4. Filter by Month
  5. Delete an Expense
  0. Exit

Adding an Expense


Choose 1 from the menu
Enter the date (or press Enter for today)
Pick a category number
Type a short description
Enter the amount in PKR


Viewing All Expenses


Choose 2 to see a full table of every recorded expense


Category Summary


Choose 3 to see how much you've spent per category, with a visual bar chart


Filtering by Month


Choose 4 and enter a month in YYYY-MM format (e.g., 2026-06)


Deleting an Expense


Choose 5, view the table, then enter the ID number of the expense to remove



📁 Project Structure

expense_tracker/
│
├── expense_tracker.py    ← Main program file
└── expenses.csv          ← Auto-created when you first add an expense


🗄️ Data Storage

Expenses are saved in a file called expenses.csv in the same folder as the script. It is created automatically on the first run.

CSV format:

id,date,category,description,amount
1,2026-06-10,Food,Lunch at cafe,350.0
2,2026-06-11,Transport,Uber ride,180.0

You can also open expenses.csv in Excel or Google Sheets to view your data.


🏷️ Categories

#Category1Food2Transport3Shopping4Entertainment5Health6Bills7Education8Other


🧠 Python Concepts Covered

This project is great for learning:


File I/O — Reading and writing files with open()
CSV Module — Structured data with DictReader and DictWriter
Functions — Modular, reusable code blocks
Input Validation — Handling bad user input gracefully
Data Structures — Working with lists of dictionaries
String Formatting — Clean table output using f-strings
DateTime — Parsing and formatting dates
Control Flow — While loops and menu-driven programs



📸 Example Output

View All Expenses:

── All Expenses ─────────────────────────────
  ID    Date         Category        Description               Amount (PKR)
  ────────────────────────────────────────────────────────────────────────
  1     2026-06-10   Food            Lunch at cafe                   350.00
  2     2026-06-11   Transport       Uber ride                       180.00
  3     2026-06-12   Health          Doctor visit                  1,200.00
  4     2026-06-14   Bills           Electricity bill              2,500.00
  ────────────────────────────────────────────────────────────────────────
  TOTAL                                                     4,230.00

Summary by Category:

── Summary by Category ──────────────────────
  Category              Total (PKR)    Share
  ────────────────────────────────────────────
  Bills                    2,500.00    59.1%  ███████████
  Health                   1,200.00    28.4%  █████
  Food                       350.00     8.3%  █
  Transport                  180.00     4.3%
  ────────────────────────────────────────────
  GRAND TOTAL              4,230.00
