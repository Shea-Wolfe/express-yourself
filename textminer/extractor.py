import re


def phone_numbers(string):
    return re.findall(r'\(?\d{3}\W*\d{3}\-?\d{4}', string)

def emails(string):
    return re.findall(r'\S+@[a-z]+\.[a-z]{2,3}', string)
