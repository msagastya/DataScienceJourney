# defaultParameter.py

def greet_user(name="Learner"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Alex")

# keyword arguments
def power(base, exp):
    return base ** exp

print(power(exp=3, base=2))  # Using keywords, order doesn’t matter