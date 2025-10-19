# Expense Tracker

import csv

def read_expense(file):
    total = 0
    try:
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total += float(row["amount"])
        print(f"Total Expense: ${total}")
    except FileNotFoundError:
        print(f"❌ File '{file}' not found!")
    except Exception as e:
        print("Unknown error:", e)

read_expense("expenses.csv")