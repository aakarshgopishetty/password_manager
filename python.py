import secrets
import string
import re

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
def check_password(password):
    if (len(password)>= 8 and 
    re.search(r"[a-z]",password) and 
    re.search(r"[A-Z]",password) and 
    re.search(r"[\d]",password) and 
    re.search(r"[!@#$%^&*(){}|<>,./?-+=`~]")):
        return "Valid Password"
    else: 
        return "Invalid Password"

password=str(input("Enter your password: "))
print(check_password(password))