#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if int(str(i)+str(j))%11!=0 and int(str(i)+str(j))<int(str(j)+str(i)):
            if int(str(i) + str(j)) == 89:
                print(f"{i}{j}")
                continue
            print(f"{i}{j}, ", end='')
