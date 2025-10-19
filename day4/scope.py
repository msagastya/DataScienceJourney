# scope.py
x = 10  # global

def modify():
    x = 5  # local
    print("Inside function:", x)

modify()
print("Outside function:", x)