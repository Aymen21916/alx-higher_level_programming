#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1_list = list(set_1)
    set2_list = list(set_2)
    common = set()
    for i in set1_list:
        for j in set2_list:
            if i == j:
                common.add(i)
    return common
