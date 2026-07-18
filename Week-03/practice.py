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
