class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Alice", [85, 90, 95])
print(f"{s1.name}'s average: {s1.average():.2f}")