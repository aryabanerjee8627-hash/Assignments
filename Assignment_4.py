#Task 1 : Read file handle error 

print("Task 1 : Read file handle error ")
n = 0
try :
    with open ("D:\\VS proj\\Assignment_4\sample.txt" , "rt") as fh:
        for line in fh:
            n += 1
            print(f'Line {n} : {line}')    
except FileNotFoundError :
    print(" Error : File not found")


#Task 2 : Appending to a file

print("\nTask 2 : Appending to a file ")
try :
    with open ("D:\\VS proj\\Assignment_4\output.txt" , "at") as FH:
     s = input(print ("Enter text to append to the file:(type 'exit' to stop)"))
     s = str(s)
     while True :
         if s != "exit":
            FH.write(s + "\n")
            s = input(print ("Enter text to append to the file:(type 'exit' to stop)"))
            s = str(s)
         else :
            break
    print("Text appended successfully.")    

    with open ("D:\\VS proj\\Assignment_4\output.txt" , "rt") as content:
        print("Content of the file after appending:")
        print(content.read())
except FileNotFoundError :
    print(" Error : File not found")

