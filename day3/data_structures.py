# data_structures.py

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Access
print(fruits[0])      # apple
print(fruits[-1])     # cherry

# Modify
fruits[1] = "mango"

# Add
fruits.append("orange")
fruits.insert(1, "kiwi")

# Remove
fruits.remove("apple")
last = fruits.pop()   # removes last element

print("Updated list:", fruits)