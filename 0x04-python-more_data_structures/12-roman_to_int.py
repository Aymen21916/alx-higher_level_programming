#!/usr/bin/python3
def roman_to_int(roman_string):   
    roman_to_int_dict = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
        "IX": 9, "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70,
        "LXXX": 80, "XC": 90, "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500,
        "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900, "M": 1000, "MM": 2000,
        "MMM": 3000
    }
    if roman_string is None or len(roman_string) == 0:
        return 0
    result = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_to_int_dict:
            result += roman_to_int_dict[roman_string[i:i+2]]
            i += 2
        else:
            result += roman_to_int_dict[roman_string[i]]
            i += 1
    return result
