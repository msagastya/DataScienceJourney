number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number2} is greater than {number1}")
else:
    print(f"Both numbers are equal: {number1} = {number2}")