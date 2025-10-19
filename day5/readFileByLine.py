# read file by line

with open("data.txt", "r") as file:
	for line in file:
		print("Fruits:", line.strip())

