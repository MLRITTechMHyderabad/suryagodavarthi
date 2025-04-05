import re

text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."
email_pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+\b'
valid_emails = re.findall(email_pattern, text)

fixed_pattern = r'\b[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+\b'
valid_emails = re.findall(fixed_pattern, text)

print(valid_emails)
