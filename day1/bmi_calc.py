weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: ")) 
# round to 2 decimal places
  
bmi = round(weight / (height ** 2),2)
print(f"Your BMI is: {bmi}")