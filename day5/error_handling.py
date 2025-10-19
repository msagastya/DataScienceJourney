# error_handling 
# try/except/finally example

try:
    print("Enter a number: ")
    num = int(input())
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer.")
finally:
    print("Execution completed.")