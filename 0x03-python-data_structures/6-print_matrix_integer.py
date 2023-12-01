#!/usr/bin/python3
if __name__ == '__main__':
    def print_matrix_integer(matrix=[[]]):
        for line in matrix:
            for num in line:
                print("{}".format(num), end=' ' if num != line[-1] else '')
            print()
