#!/usr/bin/python3
def remove_char_at(str, n):
    str = str if n < 0 else str[:n] + str[n+1:]
    return str
