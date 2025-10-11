#Task 1 : factorial of a number
print ("Task 1 : factorial of a number")
n = int(input("Enter a number to find its factorial: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
ans = factorial(n)
print(f"The factorial of {n} is {ans}")


#Task 2 : Math functions
print ("\nTask 2 : Math functions")
import math
num = float(input("Enter a number to find its square root, logarithm and sine: "))
sqrt = math.sqrt(num)
log = math.log(num)
sine = math.sin(num)
print(f"The square root of {num} is {sqrt}")
print(f"The natural logarithm of {num} is {log}")
print(f"The sine of {num} is {sine}")