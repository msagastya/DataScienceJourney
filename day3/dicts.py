# dicts.py
student = {
    "name": "Alex",
    "age": 25,
    "marks": [85, 90, 92]
}

print(student["name"])
print(student.get("age"))
student["city"] = "New York"      # add new key
student["age"] = 26               # update
print(student.keys())
print(student.values())
print(student.items())