import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    return re.findall(pattern, text)

input_text = input("Enter text to search for emails: ")
emails = find_emails(input_text)
print("Found emails:", emails)