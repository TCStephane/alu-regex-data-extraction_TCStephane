import re
import json

with open("input/raw-text.txt", "r") as f:
    text = f.read()

email_pattern = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'
all_mails = re.findall(email_pattern, text)

def is_safe_email(email):
    if any(char in email for char in ["'", '"', "<", ">", ";", "--"]):
        return False
    
    if email.count("@") != 1:
        return False
    
    if ".." in email.split("@")[1]:
        return False
    
    return True