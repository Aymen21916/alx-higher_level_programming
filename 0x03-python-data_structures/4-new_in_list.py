#!/usr/bin/python3
if __name__ == '__main__':
    def new_in_list(my_list, idx, element):
        new_list = []
        for n in my_list:
            new_list.append(n)
        if idx < 0 or idx >= len(my_list):
            return my_list
        new_list[idx] = element
        return new_list
