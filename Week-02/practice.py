
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


#Challenge 4: List of movies from user
movies = []
for i in range(0,5):
    names = input("Enter the movie name: ")
    movies.append(names)
print(movies)

#Challenge 5: Number list
nums = [50,60,20,10,30,40,100,90]
avg = sum(nums)/len(nums)
print("Maximum: ",max(nums))
print("Minimum: ",min(nums))
print("Sum: ",sum(nums))
print("Average: ",avg)

#Challenge 6: Check Availability in list
fruits = ['Apples','Oranges','Bananas','Grapes','Kiwi']
name = input("Enter name you want to check: ")
if name in fruits:
    print("Available")      
else:
    print("Not available")
        
#Challenge 7:
nums = []
for i in range(0,5):
    num = int(input("Enter the number: "))
    nums.append(num)
sorted_list = sorted(nums)
print("Original: ",nums)
print("Sorted: ",sorted_list)
print("Maximum number of list: ",max(nums))
print("Minimum number of list: ",min(nums))
