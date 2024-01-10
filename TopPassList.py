import re

def is_valid_password(password):
    """
    Check if the password meets all five criteria:
    1. Must contain uppercase
    2. Must contain lowercase
    3. Must contain numbers
    4. Must contain special characters
    5. Password length must be equal to or more than 8 characters
    """
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    is_correct_length = len(password) >= 8
    
    return all([has_upper, has_lower, has_digit, has_special, is_correct_length])

def filter_passwords(input_file, output_file):
    """
    Read passwords from input_file, filter them, and write valid passwords to output_file.
    """
    with open(input_file, 'r') as file:
        passwords = file.readlines()

    valid_passwords = [pw.strip() for pw in passwords if is_valid_password(pw.strip())]

    with open(output_file, 'w') as file:
        for pw in valid_passwords:
            file.write(pw + '\n')

# Example usage
input_file = '10-million-password-list-top-1000000.txt'  # Replace with your file path
output_file = 'out.txt' # Output file name

filter_passwords(input_file, output_file)