#!/usr/bin/python3
if __name__ == '__main__':
    def max_integer(my_list=[]):
        if my_list is None:
            return None
        max = my_list[0]
        for num in my_list:
            if num > max:
                max = num
        return max
