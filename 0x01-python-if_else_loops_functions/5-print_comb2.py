#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
        break
    print(f"{i:02}, ", end='')
