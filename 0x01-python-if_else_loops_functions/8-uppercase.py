#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for s in str:
        if s >= 'a' and s <= 'z':
            upper += chr(ord(s) - ord('a') + ord('A'))
        else:
            upper += s
    print("{}".format(upper))
