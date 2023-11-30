#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument.".format(n))
        print("{}: {}".format(n, sys.argv[n]))
    else:
        print("{} arguments:".format(n))
        for i in range(0, n):
            print("{}: {}".format(i+1, sys.argv[i+1]))
