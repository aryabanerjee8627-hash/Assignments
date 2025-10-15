#Task 1 : Fetching marks from student dictionary
print("Task 1 : Fetching marks from student dictionary")
records = {'Alice': 85, 'Ozzy': 80, 'Charles': 78 , 'David': 92, 'Eve': 88}

n = input("Enter the name of the student: ")
if n in records:
    print(f"{n}'s marks are: {records[n]}")
else:
    print("Student not found in records.")


#Task 2 : Extraction from list and print in reverse order
print("\nTask 2 : Extraction from list and print in reverse order")
l1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] 
print (f"Original list :{l1}")
l1 = l1[0:5:1]
print(f"Extracted first five elements :{l1}")
l1.reverse()
print(f"Extracted elements in reverse order :{l1}")