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