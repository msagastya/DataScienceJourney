# Write File

fruits = ["strawberry", "pineapple", "kiwi"]
with open("data.txt", "w") as file:
	for fruits in fruits:
		file.write(fruits + "\n")

print("Data written successfully")
