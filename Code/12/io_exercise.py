# 正则库
import re

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)

def pruetext(text):
    tmptxt = re.sub("[\W_]+", "", text)
    newtmptxt = tmptxt.lower()
    return newtmptxt

something = input("Enter text: ")
something = pruetext(something)
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")