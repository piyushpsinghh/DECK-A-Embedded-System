import re

def uppercase_check(password):
    if re.search('[A-Z]', password): #atleast one uppercase character
        return True
    return False

def lowercase_check(password):
    if re.search('[a-z]', password): #atleast one lowercase character
        return True
    return False

def digit_check(password):
    if re.search('[0-9]', password): #atleast one digit
        return True
    return False


def IsStrong():
    password = input("Enter password : ")
        #atleast 8 character long
    if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password):
        print("Strong Password")
    else:
        print("Weak Password")

# IsStrong()
#kartik