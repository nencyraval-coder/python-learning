#=========================
# Week 2 - Strings
#=========================

print("\n========== Strings ==========")
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

#Exercise 7: strip()
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
print("\n---------- join() ----------")
fruits = ["Apple", "Banana", "Mango"]
result = " - ".join(fruits)
print(result)

#Exercise 14
print("\n---------- isalpha() ----------")
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