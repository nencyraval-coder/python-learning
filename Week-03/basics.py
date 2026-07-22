"""#Creating and accessing a dictionary
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
    print("File not found.") """
# MODULES AND LIBRARIES
# 1 math module
import math
print("Square root: ",math.sqrt(64))
print("Power: ",math.pow(5,3))
print("Pi value: ",math.pi)
print("Floor: ", math.floor(8.9))
print("Ceil: ", math.ceil(8.6))

# 2 random
import random
print("Random module:", random.randint(1,100) )
colors = ['red','blue','yellow','green','purple']
print("Random color: ", random.choice(colors))

# date and time
import datetime
today = datetime.datetime.now()
print("Current Date:", today.date())
print("Current Time:", today.time())
print("Year:", today.year)
print("Month:", today.month)
# own module
# create own .py file with diff funcs and later you can use them
#  OBJECT-ORINENTED PROGRAMMING (OOP)
# single object
class student:
    name = 'Alex'
    age = 20
student1 = student()
print(student1.name())
print(student1.age)
# multiple object
## student
class student:
    name = ''
    age = 0

student1 = student()
student2 = student()

student1.name = 'Rahul'
student1.age = 20

student2.name = 'Priya'
student2.age = 19

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
class Car:
    brand = ""
    price = 0
## car
car1 = Car()

car1.brand = "Toyota"
car1.price = 1500000

print(car1.brand)
print(car1.price)
