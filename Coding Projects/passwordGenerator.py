#The random class will be used to randomly choose characters
#The string class will supply us with the characters to be randomly selected
import random
import string

#Creates a list with all viable characters
supportedChars = string.ascii_letters + string.digits + string.punctuation

#Asks the user how long they would like the password to be
passwordLength = int(input("Enter password length (at least 12 is recommended): "))

#Randomly generates passwordLength characters from the supportedChars list and adds them to the password
password = ""
for i in range(passwordLength):
    password += supportedChars[random.randint(0, len(supportedChars))]

#Outputs the password
print(password)