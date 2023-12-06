#!/usr/bin/python3
def uniq_add(my_list=[]):
    done = []
    s = 0
    for i in my_list:
        d = False
        for j in done:
            if i == j:
                d = True
        if not d:
            s += i
            done.append(i)
    return s
