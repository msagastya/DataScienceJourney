# Grading System

def comput_grade (score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'
    
def summary(students):
    for name, score in students.items():
        grade = comput_grade(score)
        print(f"{name}: Score={score}, Grade={grade}")

students_scores = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "David": 45,
    "Eve": 30
}

summary(students_scores)