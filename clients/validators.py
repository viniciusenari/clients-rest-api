import re

def valid_ssn(value):
    regex = '^(?!666|000|9\\d{2})\\d{3}(?!00)\\d{2}(?!0{4})\\d{4}$'
    return re.search(regex, value)
    
def valid_name(value):
    return value.isalpha()

def valid_phone_number(value):
    regex = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    return re.search(regex, value)