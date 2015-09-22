import re


def phone_numbers(string):
    return re.findall(r'\(?\d{3}\W*\d{3}\-?\d{4}', string)
