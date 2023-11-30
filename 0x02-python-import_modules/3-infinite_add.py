#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    for n in sys.argv[1:]:
        s += int(n)
    print("{:d}".format(s))
