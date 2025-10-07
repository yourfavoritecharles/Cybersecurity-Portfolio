### This password strength checking program uses the Microsoft account password requirements as a baseline
### Microsoft requires a minimum length of 8 characters, which I bumped up to 14 for security purposes
### Microsoft has a maximum length for passwords, but I ignored that for security purposes
### Microsoft requires at least three of the four categories: Lowercase letters, uppercase letters, numbers, symbols. I decided to require all of them to enhance security

#Imports the string module for complexity checking
import string

#Receives a password from the user
password = str(input("Please enter a password: "))
print("-----------------------------------")

#Imports a file of the 10000 most common passwords in read mode
commonPasswords = open("Sources/commonPasswords.txt","r")
commonPasswordsLines = commonPasswords.read().splitlines()

#If hasIssue remains False, it will tell the user that their password is okay
hasIssue = False

#Looks through the 10000 most common passwords and sets isCommon and hasIssue to True if the user-given password is in the list
isCommon = False
for line in commonPasswordsLines:
    if(password == line):
        isCommon = True
        hasIssue = True

#Tells the user if their password is common or not long enough
#If the password is not long enough, hasIssue is set to True
if(isCommon):
    print("Your password has been detected in a list of common passwords, which makes it easy for hackers to guess it. Try changing your password to something more unique!")
if(len(password) < 14):
    print("We recommend making your password at least 14 characters long!")
    hasIssue = True

#Looks through each character of password to determine if it meets complexity requirements (has lowercase letters, uppercase letters, numbers, and supported symbols)
isSimple = True
hasNumber = False
hasLower = False
hasUpper = False
hasSymbol = False
for char in password:
    if(char.isdigit()):
        hasNumber = True
    elif(string.ascii_lowercase.find(char) != -1):
        hasLower = True
    elif(string.ascii_uppercase.find(char) != -1):
        hasUpper = True
    elif(string.punctuation.find(char) != -1):
        hasSymbol = True

#Tells the user which complexity requirements they have not met
#hasIssue is set to True when a complexity requirement is not met
if(not hasNumber):
    print("You must include a number in your password")
    hasIssue = True
if(not hasLower):
    print("You must include a lowercase letter in your password")
    hasIssue = True
if(not hasUpper):
    print("You must include an uppercase letter in your password")
    hasIssue = True
if(not hasSymbol):
    print("You must include a symbol in your password")
    hasIssue = True

#Congratulates the user if hasIssue remained False
if(not hasIssue):
    print("Your password meets our standards! Make sure to change your password regularly and use Two Factor Authentication!")