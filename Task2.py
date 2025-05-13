import re

def is_valid_email(email):
    # Basic email pattern: something@something.something
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage:
print(is_valid_email("user@domain.com"))  # Output: True
print(is_valid_email("user@domain"))      # Output: False
print(is_valid_email("userdomain.com"))   # Output: False
print(is_valid_email("user@domain.co.in")) # Output: True
