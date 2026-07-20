#Creating and accessing a dictionary
student = {"name":"Alex", "Roll no.": 20, "Branch": "CSE", "CGPA": 8.7}
print(student)
print("Name:",student["name"])
print("Roll no.:",student["Roll no."])
print("Branch:",student["Branch"])
print("CGPA:",student["CGPA"])
student["CGPA"] = 9.3
student["Grade"] = "A" #Adding and updating values
print(student)
#dictionary methods
print(student.values())
print(student.keys())
print(student.items())
print(student.get("name"))
key = input("Enter the key you want to search: ")
if key in student:
    print("Key exists")
else:
    print("Doesn't Exist")
# FILE HANDLING
    # Writing in a file
file = open("notes.txt","w")

file.write("Hello Python!\n")
file.write("Learning File Python")

file.close()
    # Reading in a file
file = open("notes.txt","r")
# line by line
for line in file:
    print(line)
#reads one line
print(file.readline())

content = file.read() #complete thing

print(content)
file.close()
    # Appending data
# This is the recommended way because Python automatically closes the file.
with open("notes.txt", "a") as file:
    file.write("\nPython is awesome!")

file.close()
print("New data added.")
# An exception is an error that occurs while the program is running.
# 1 try and except
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except:
    print("Something went wrong!")

# 2 catch specific errors
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 3 else runs only if no exception occurs.
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Answer:", result)

# 4 finally always runs, whether there is an error or not.
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Execution completed.")
# 5 file handling exceptions
try:
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")