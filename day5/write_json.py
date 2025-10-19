import json

person = {"name" : "Suyash Mishra", "age" : 25, "skills" : ["ML", "AI"]}
with open("person.json", "w") as f:
	json.dump(person, f, indent=4)
