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