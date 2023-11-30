#!/usr/bin/python3
import sys
s = 0
for n in sys.argv[1:]:
    s += int(n)
print("{:d}".format(s))
