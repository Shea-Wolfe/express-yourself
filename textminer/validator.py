import re
def binary(string):
    return re.match(r'\s*[0-1]+$',string)

def binary_even(string):
    return re.match(r'[0-1]+$', string)
