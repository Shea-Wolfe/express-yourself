import re
def binary(string):
    return re.match(r'\s*[0-1]+$',string)

def binary_even(string):
    return re.match(r'\s*[0-1]+0$', string)

def hex(string):
    return re.match(r'[0-9A-F]+$',string)
