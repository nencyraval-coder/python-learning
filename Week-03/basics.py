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