# factorial (without using recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(100))  # Output: 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000
