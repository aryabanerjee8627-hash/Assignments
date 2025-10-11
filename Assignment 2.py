#Task 1 :  Even Odd checker
print("Even Odd Checker")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is an Even number")
else:
    print(f"{n} is an Odd number")


#Task 2 :  Sum upto 50
print("Sum of numbers from 1 to 50")
sum = 0
for i in range(1, 51):
    sum += i
print(f"The sum of numbers from 1 to 50 is:", {sum})
