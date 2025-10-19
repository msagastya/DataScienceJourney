# CSV writer
import csv

with open("scores.csv", "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["name","marks"])
	writer.writerows([["Alex", 88], ["Sam", 95]])
