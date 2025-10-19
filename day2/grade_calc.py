# grade_calc.py

score = int(input("Enter your score: "))
if score < 40:
    print("Fail")
elif score < 60:
    print("Pass")
elif score < 80:
    print("Merit")
else:
    print("Distinction")