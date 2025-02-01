import secrets
import string
import re

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
def check_password(password):
    points=0
    if (len(password)>= 8 ):
        points+=1
    if re.search(r"[a-z]",password):
        points+=1
    if re.search(r"[A-Z]",password):
        points+=1 
    if re.search(r"[\d]",password):
        points+=1
    if re.search(r"[!@#$%^&*(){}|<>,./?\-+=`~]", password):
        points+=1
    if points!=0:
        if points==1:return "Needs Improvement"
        elif points==2:return "Bad"
        elif points==3:return "Average"
        elif points==4:return "Good"
        elif points==5:return "Perfect"
    else: 
        return "Invalid Password"

password=str(input("Enter your password: "))
print(check_password(password))