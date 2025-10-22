class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_report(self):
        print("Class Report:")
        for s in self.students:
            print(f"{s.roll} - {s.name} : {s.average():.2f}")

s1 = Student("Alice", 1, [90, 80, 85])
s2 = Student("Bob", 2, [70, 75, 80])
s3 = Student("Charlie", 3, [95, 92, 90])

room = Classroom()
room.add_student(s1)
room.add_student(s2)
room.add_student(s3)
room.show_report()