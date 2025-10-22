import csv

class Dataset:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load(self):
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            self.data = [row for row in reader]
        print(f"Loaded {len(self.data)} rows.")

    def get_column(self, col_name):
        return [row[col_name] for row in self.data]

dataset = Dataset("scores.csv")   # reuse file from Day 5
dataset.load()
print("Names:", dataset.get_column("name"))
print("Marks:", dataset.get_column("marks"))