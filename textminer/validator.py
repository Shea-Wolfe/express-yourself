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
            return None
        else:
            pass
    if None in [word(s) for s in ret]:
        return None
    else:
        return ret

def phone_number(string):
    return re.match(r'.*\d{3}\W*\d{3}\W*\d{4}$',string)

def money(string):
    return re.match(r'\$[0-9]{1,3}(\,[0-9]{3}|[0-9]{0,3})*(\.[0-9]{2})?$', string)

def zipcode(string):
    return re.match(r'\d{5}(\-\d{4})?$', string)

def date(string):
    return re.match(r'\d{4}[\/\-]{1}\d{2}[\/\-]{1}\d{2}|\d{1,2}[\/\-]{1}\d{1,2}[\/\-]{1}\d{4}',string)

def hdate(string):
    return re.match(r'([A-Z]{1}[a-z]*\.? (?=[0-2]\d|[1-9]\W|30|31)|0?2\W*(?=([0-2]\d|[0-9]\W))|(0?1|0?[3-9]|1[0-2])\W*(?=([0-2]\d|30|31|[0-9]\W))|[12][0-9]{3}\W)'
                    r'([A-Z]{1}[a-z]*\.? (?=[0-2]\d|[1-9]\W|30|31)|0?2\W*(?=([0-2]\d|[0-9]\W))|(0?1|0?[3-9]|1[0-2])\W*(?=([0-2]\d|30|31|[0-9]\W))|[0-2]?[0-9]\W|30\W|31\W)'
                    r'([0-2]?[0-9]$|30$|31$|[1-2][0-9]{3}$)', string)
