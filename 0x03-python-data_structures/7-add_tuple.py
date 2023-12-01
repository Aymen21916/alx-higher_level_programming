#!/usr/bin/python3
if __name__ == '__main__':
    def add_tuple(tuple_a=(), tuple_b=()):
        tuple_a_copy, tuple_b_copy = (), ()
        if len(tuple_a) > 2:
            tuple_a_copy = tuple_a[0:1]
        elif len(tuple_a) < 2:
            tuple_a_copy = (tuple_a[0], 0)
        elif len(tuple_a) == 0:
            tuple_a_copy = (0, 0)
        else:
            tuple_a_copy = tuple_a
        if len(tuple_b) > 2:
            tuple_b_copy = tuple_b[0:1]
        elif len(tuple_b) == 1:
            tuple_b_copy = (tuple_b[0], 0)
        elif len(tuple_b) == 0:
            tuple_b_copy = (0, 0)
        else:
            tuple_b_copy = tuple_b
        tuple = (tuple_a_copy[0] + tuple_b_copy[0], (tuple_a_copy[1] + tuple_b_copy[1]))
        return tuple
