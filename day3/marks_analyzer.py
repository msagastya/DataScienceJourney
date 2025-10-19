# marks_analyzer.py

students = {
    "Alice": [78, 85, 90],
    "Bob": [60, 65, 70],
    "Charlie": [90, 95, 92]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name}'s average marks: {avg:.2f}")

# Find top scorer
averages = {name: sum(m)/len(m) for name, m in students.items()}
top_student = max(averages, key=averages.get)
print(f"\n🏆 Top Student: {top_student} with {averages[top_student]:.2f}")