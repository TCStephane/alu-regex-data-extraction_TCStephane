import re
import json

with open("input/raw-text.txt", "r") as f:
    text = f.read()

email_pattern = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'
