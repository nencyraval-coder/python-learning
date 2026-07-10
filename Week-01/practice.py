#Exercise 1: Area of Rectangle
l=float(input("Enter the length of rectangle: "))
b=float(input("Enter the breadth of rectangle: "))
a=l*b
print("Area of rectangle is: ",a)

#Exercise 2: Asking Details from user
n=input("Enter your name: ")
a=int(input("Enter your age: "))
c=input("Enter your city: ")
print("Name:", n)
print("Age:", a)
print("City:", c)

#Exercise 3: Area of Circle
r=float(input("Enter the radius of circle: "))  
area=3.14*r*r
print("Area of circle is: ", area)

#Exercise 4: Student Report
print("---------- Student Report ----------")
name = input("\nEnter your name: ")
age = int(input("\nEnter your age: "))
branch = input("\nEnter your branch: ")
cgpa = float(input("\nEnter your CGPA: "))
print("\n---------- RESULT ----------")
print("\nName:", name)
print("\nAge:", age)
print("\nBranch:", branch)
print("\nCGPA:", cgpa)

#Exercise 5: BMI Calculator
print("---------- BMI Calculator ----------")
weight = float(input("\nEnter your weight in kg: "))
height = float(input("\nEnter your height in m: "))
bmi = weight / (height ** 2)
print("\n---------- RESULT ----------")
print("\nYour BMI is:", round(bmi, 2))
print("\n \nThank you for using the BMI Calculator.")

#Excercise 6: Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Exercise 7: Even or Odd
print("\n-------- Even or Odd --------")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("\nThe number is even.")
else:
    print("\nThe number is odd.")

#Exercise 8: Grade Calculator
print("\n-------- Grade Calculator --------")
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Exercise 9: Largest of Two Numbers
print("\n-------- Largest of Two Numbers --------")
num1 = float(input("Enter first number: "))     
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("\nThe largest number is:", num1)
elif num2 > num1:
    print("\nThe largest number is:", num2)
else:
    print("\nThe numbers are equal.")

#Exercise 10: ATM Login
print("\n-------- ATM Login --------")

account = input("\nDo you have an account? (yes/no): ")

if account == "yes":
    pin = int(input("Enter PIN: "))
    if pin == 1234:
        print("Access Granted")
    else:
        print("Wrong PIN")
else:
    print("Please create an account.")

#Exercise 11: Driver's License Eligibility
print("-------- Driving Eligibility --------")

age = int(input("\nEnter your age: "))
license = input("\nDo you have a driving license? (yes/no): ")

if age >= 18:

    if license == "yes":
        print("You can drive.")
    else:
        print("Get your driving license first.")

else:
    print("You are underage.")

#Exercise 12: Successful Login
print("\n-------- Successful Login --------")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "python123":
    print("Login successful!")
else:
    print("Invalid username or password.")

#Exercise 13: Checking Positive, Negative or Zero
print("\n-------- Positive, Negative or Zero --------")
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Exercise 14: Leap Year Checker
print("\n-------- Leap Year Checker --------")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#Exercise 15: Simple Calculator
print("\n-------- Simple Calculator --------")  
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
result = None
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print("Result:", result) 

#Exercise 16: !-10 using for loop
for i in range(0,10):
    print(i+1)
    i+=1

#Exercise 17: print even no.s using for loop
for i in range(2,21,2):
    print(i)

#Exercise 18: Table
print("\n-------- Table --------")
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Exercise 19: Sum of First N Numbers
print("\n-------- Sum of First N Numbers --------")
num=int(input("Enter the end number: "))
sum=0
for i in range(0,num):
    sum=sum+i
print("The sum of first",num,"numbers is:",sum)

#Exercise 20: Factorial of a Number
print("\n-------- Factorial of a Number --------")
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is:",fact)

#Exercise 21: Reverse Table
print("\n-------- Reverse Table --------")
num=int(input("Enter a number: "))
for i in range(10,0,-1):
    print(num,"x",i,"=",num*i)

#Exercise 22: Password Checker
print("\n-------- Password Checker --------")

password = ""

while password != "python":
    password = input("Enter password: ")

print("Access Granted!")