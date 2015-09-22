import re
import textminer.validator as v

def words(string):
    return v.words(string)

def phone_number(string):
    phone_book = {}
    if not v.phone_number(string):
        return None
    ret = re.sub(r'[^0-9]','',string)
    phone_book['area_code'] = ret[:3]
    phone_book['number'] = '{}-{}'.format(ret[3:6],ret[6:])
    return phone_book

def money(string):
    money_dict = {}
    if not v.money(string):
        return None
    money_dict['currency'] = string[0]
    ret = re.sub(r'[^0-9\.]', '', string)
    money_dict['amount'] = float(ret[0:])
    return money_dict
