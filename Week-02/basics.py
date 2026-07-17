
name = "Nency"
city = "Ahmedabad"
college = "GTU"
print(name)
print(city)
print(college)

#string Indexing
word = "Python"
print("\nWord : ", word)
print("First Letter: ",word[0])
print("Second Letter: ",word[1])
print("Last Letter: ",word[5])

#negative indexing
word = "Programming"
print("\nWord : ", word)
print("Last Letter: ",word[-1])
print("Second Last Letter: ",word[-2])
print("Third Last Letter: ",word[-3])

#Sting slicing
text = "Artificial Intelligence"
print("\nOriginal word: ",text)
print(text[0:10])
print(text[11:])
print(text[:10])
print(text[-12:])

#Length of string
sentence = input("Enter a sentence: ")
print("Length of the sentence: ", len(sentence))    

#upper and lower case
text = input("Enter a text: ")
print("Lowercase: ",text.lower())
print("Uppercase: ",text.upper())

#Exercise 7: strip() [removes whitespace from the beginning and end of the string]
text = input("\nEnter something with spaces: ")
print("Before:", text)
print("After :", text.strip())

#Exercise 8: replace()
sentence = "I like Java"
print(sentence.replace("Java", "Python"))

#Exercise 9: find()
sentence = "Python is easy"
print(sentence.find("easy"))
print(sentence.find("Java"))

#Exercise 10: count()
text = "banana"
print(text.count("a"))
print(text.count("n"))

#Exercise 11
email = input("\nEnter your email: ")
print(email.startswith("n"))
print(email.endswith(".com"))

#Exercise 12
print("\n---------- split() ----------")
sentence = input("Enter your full name: ")
words = sentence.split()
print(words)

#Exercise 13 
fruits = ["Apple", "Banana", "Mango"]
result = " - ".join(fruits)
print(result)

#Exercise 14
text = input("Enter text: ")
print(text.isalpha())
print(text.isdigit())
print(text.isalnum()) 
print(name.capitalize()) #Capitalizes the first letter of the string
print(city.title()) #Capitalizes the first letter of each word in the string
print(text.swapcase()) #Changes uppercase letters to lowercase and vice versa

#Exercise 15: Slicing (The end index is not included.)
text = "Python"
print(text[-1])
print(text[-6])
word = "Programming"
print("\n",word[4:11])
print(word[:9])
print(word[3:])
print(word[-7:-1])
print(word[::-1]) #reverse

#Lists
fruits = ["Apples", "Bananas", "Mango", "Orange"]
print(fruits[-1]) #Accessing Elements
print(fruits[0])
fruits[1] = "Grapes" #Changing Element
#list methods
nums = [10,20,30,70]
nums.pop()
nums.append(40)
nums.insert(1,60)
nums.remove(10)
print(nums)
print(fruits)
#TUPLES AND SETS
colors = ("Red", "Green", "Blue") #Tuple
print(colors[0])
# colors[1] = "Black"   This will give an error, since tuples are immutable
fruits = {"Apple", "Banana", "Mango", "Mango"} #Set
print(fruits) #Output order may vary because sets are unordered.
# Duplicates are removed automatically.
#FUNCTIONS
def greet():
    print("Hello!")
    print("Welcome to Python.")
greet()
#function with parameters (A parameter lets us send data into a function.)
def greet(name):
    print("Hello,", name)
greet("Alice")
greet("Bob")
greet("Charlie")
#function w return value
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)
#Function with Multiple Parameters
def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)
student("Rahul", 20, "CSE")
#function with default parameter
def greet(name="Guest"):
    print("Hello,", name)
greet()  # Uses default value
greet("Alice")  # Overrides default value
#arguments and keyword arguments
def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)
student(name="Rahul", age=20, branch="CSE")  # Using keyword arguments
#multiple return values
def calculate(a, b):
    return a + b, a - b, a * b, a / b
sum_result, diff_result, prod_result, div_result = calculate(10, 5)
#global and local variables
x = 10  # Global variable (accessible throughout the program)
def print_values():
    y = 5  # Local variable (only accessible within this function)
    print("Inside function - x:", x)
    print("Inside function - y:", y)
