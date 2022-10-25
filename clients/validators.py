def valid_ssn(value):
    return len(value) == 9
    
def valid_name(value):
    return value.isalpha()

def valid_phone(value):
    return value.isdigit() and len(value) >= 10