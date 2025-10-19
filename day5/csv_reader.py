# CSV reader
import csv

with open("scores.csv", "r") as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
