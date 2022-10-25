import re

def valid_ssn(value):
    return len(value) == 9
    
def valid_name(value):
    return value.isalpha()

def valid_phone_number(value):
    format = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    return re.search(format, value)