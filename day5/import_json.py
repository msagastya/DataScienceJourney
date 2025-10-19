import json

with open("person.json", "r") as f:
	data = json.load(f)
	print("Name: " , data["name"])
	print("Skills: " , ", ".join(data["skills"]))
