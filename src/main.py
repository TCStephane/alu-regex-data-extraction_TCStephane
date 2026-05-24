import re
import json

with open("input/raw-text.txt", "r") as f:
    text = f.read()

email_pattern = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'
card_pattern = r'\b\d{4}[\s-]\d{4,6}[\s-]\d{4,6}[\s-]\d{3,4}\b'
all_mails = re.findall(email_pattern, text)
all_cards = re.findall(card_pattern, text)

def is_safe_email(email):
    if any(char in email for char in ["'", '"', "<", ">", ";", "--"]):
        return False
    
    if email.count("@") != 1:
        return False
    
    if ".." in email.split("@")[1]:
        return False
    
    return True

safe_emails = [e for e in all_mails if is_safe_email(e)]

alu_domains = ["@alueducation.com", "@alumni.alueducation.com", "@si.alueducation.com"]

alu_emails = [e for e in safe_emails if any(e.endswith(d) for d in alu_domains)]
general_emails = [e for e in safe_emails if not any(e.endswith(d) for d in alu_domains)]

print("\n\nGeneral Emails: ", general_emails)
print("\n\nALU Emails: ", alu_emails)

def is_valid_card(card):
    digits_only = re.sub(r'[\s-]', '', card)

    if not digits_only.isdigit():
        return False

    if not (15 <= len(digits_only) <= 16):
        return False
    return True

safe_cards = [c for c in all_cards if is_valid_card(c)]

def mask_card(card):
    digits_only = re.sub(r'[\s-]', '', card)
    return "**** **** ****" + digits_only[-4:]

masked_cards = [mask_card(c) for c in safe_cards]

print("\n\nCredit Cards (masked):", masked_cards)