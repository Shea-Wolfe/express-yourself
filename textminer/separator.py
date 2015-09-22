import re
import textminer.validator as v

def words(string):
    return v.words(string)

def phone_number(string):
    if not v.phone_number(string):
        return None
    else:
        pass
