# Dictionary
# 1 
stu = {}
stu['name'] = input("Enter name: ")
stu['roll'] = int(input("Enter roll no.: "))
stu['age'] = int(input("Enter age: "))
stu['cgpa'] = float(input("Enter cgpa: "))
print(stu)
for key, value in stu.items():
    print(key, ':', value)
# 2 
marks = {'Math': 99, 'Science': 97, 'English': 95, 'Social Science':94}
highest = max(marks, key=marks.get)
print("Highest scoring subject:", highest)
print("Marks:", marks[highest])

# 3 Phone directory
phonebook = {}
for i in range(3):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phonebook[name] = number
search = ("Enter the name you want to search: ")
if search in phonebook:
    print(search,":",phonebook[search])
else:
    print("Not found")

# 4 
products = {
    "Laptop": 65000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 9000,
    "Headphones": 2000
}

name = input("Enter product name: ")
if name in products:
    print("Price of",name ,":",products[name])
else:
    print("Product not found")
# 5 Count frequncy
numbers = [1,2,3,2,1,4,5,2,1,3]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
    
print(frequency)
# 6 Login System
users = {
    "admin": "1234",
    "student": "python",
    "guest": "guest123"
}
username = input("Username: ")
password = input("Password: ")
if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
# 7 Shopping Cart
products = {
    "Laptop":65000,
    "Mouse":500,
    "Keyboard":1200,
    "Monitor":9000
}
total = 0
while True:
    item = input("Enter the item name or'done': ")
    if item.lower() == 'done':
        break
    if item in products:
        total+= products[item]
        print("Added",item)
    else:
        print("Product not found")

print("Total bill:",total)
# 8 Employee details
employees = {
    "Amit":45000,
    "Priya":52000,
    "Rahul":48000,
    "Sneha":60000
}
highest_salary = max(employees, key= employees.get)
lowest_salary = min(employees, key= employees.get)
average = sum(employees.values()) / len(employees)
print("Highest salary:",highest_salary)
print("Lowest salary:",lowest_salary)
print("Average salary:",average)
# FILE HANDLING
# 1 DIARY
diary = input("Write today's note: ")
with open("diary.txt", "a") as file:
    file.write(diary + "\n")
print("Diary saved.")
# 2 Counting no. of chars
with open("notes.txt", "r") as file:
    text = file.read()
print("Characters:", len(text))
# 3 Counting no. of lines
with open("notes.txt", "r") as file:
    lines = file.readlines()
print("Total lines:", len(lines))
# 4 Feedback system
feedback = input("Enter feedback: ")
with open("feedbacks.txt","a") as file:
    file.write(feedback + "\n")
print("Feedback saved!\n")
print("All feedbacks:\n")
with open("feedbacks.txt","r") as file:
    feeds = file.read()
print(feeds)