import re
def binary(string):
    return re.match(r'\s*[0-1]+$',string)

def binary_even(string):
    return re.match(r'\s*[0-1]+0$', string)

def hex(string):
    return re.match(r'[0-9A-F]+$',string)

def word(string):
    return re.match(r'\w*-*[A-Za-z]+$',string)

def words(string, count=None):
    ret = re.split(' ', string)
    if count:
        if count != len(ret):
            return False
        else:
            pass
    if None in [word(s) for s in ret]:
        return False
    else:
        return True

def phone_number(string):
    return re.match(r'.*\d{3}\W*\d{3}\W*\d{4}$',string)

def money(string):
    return re.match(r'\$[0-9]{1,3}(\,[0-9]{3}|[0-9]{0,3})*(\.[0-9]{2})?$', string)
