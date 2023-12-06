#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    else:
        s = 0
        b = 0
        for i in my_list:
            s +=  i[0] * i[1]
            b += i[1]
        return s / b
