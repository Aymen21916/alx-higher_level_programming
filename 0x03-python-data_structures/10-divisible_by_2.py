#!/usr/bin/python3
if __name__ == '__main__':
    def divisible_by_2(my_list=[]):
        list = []
        for x in my_list:
            if x % 2 == 0:
                list.append(True)
                continue
            list.append(False)
        return list
