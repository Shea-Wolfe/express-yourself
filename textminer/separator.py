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

def zipcode(string):
    zip_disk = {}
    if not v.zipcode(string):
        return None
    ret = re.sub('[^0-9]','', string)
    if len(ret) == 9:
        zip_disk['zip'] = ret[:5]
        zip_disk['plus4'] = ret[5:]
    else:
        zip_disk['zip'] = ret[:5]
        zip_disk['plus4'] = None
    return zip_disk

def date(string):
    dates = {}
    if not v.date(string):
        return None
    ret = re.split(r'[\/\-]', string)
    if len(ret[0]) == 4:
        dates['year'] = int(ret[0])
        dates['month'] = int(ret[1])
        dates['day'] = int(ret[2])
    else:
        dates['year'] = int(ret[2])
        dates['month'] = int(ret[0])
        dates['day'] = int(ret[1])
    return dates
