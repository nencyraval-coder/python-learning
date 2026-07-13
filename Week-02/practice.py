
str = "Nency Raval"
print("Original: ",str)
print("Upper case:",str.upper())
print("Lower case: ",str.lower())
print("Total letters: ",len(str))
print("Starts with N: ",str.startswith("N"))
print("Ends with l: ",str.endswith("l"))

#Username Validator
username = input("Enter the username: ")
if (len(username)>=5 and username.isalnum):
    print("Valid Username")
else:
    print("Invalid Username")

#Password Strength Checker
password = input("Enter the password: ")
if (len(password)>=8 and password.isdigit):
    print("Strong Password")
else:
    print("Try another Password")

#Email checker
email_id = input("Enter the email: ")
if ('@' in email_id and email_id.endswith('.com')):
    print("Email is Valid")
else:
    print("Invalid Email")

#Challenge 1
word = input("Enter the word: ")
print("The first character of word: ",word[0])
print("The last character of word is: ",word[-1])
print("The no. of characters: ",len(word))

#Challenge 2
sentence = input("Enter the sentence: ")
print("The first 5 characters are: ",sentence[:5])
print("The last 5 characters are: ",sentence[-5:])
print("The reverse of the sentence is: ",sentence[::-1])

#Challenge 3: Check if input is palindrome/not
word = input("Enter the word: ")
rev = word[::-1]
if (word == rev):
    print("Palindrome")
else:
    print("Not palindrome")