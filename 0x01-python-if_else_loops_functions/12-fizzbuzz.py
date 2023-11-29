#!/usr/bin/python3
def fizzbuzz():
    end=' '
    for i in range(1, 101):
        if i == 100:
            end = ''
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=end)
        elif i % 3 == 0:
            print("Fizz", end=end)
        elif i % 5 == 0:
            print("Buzz", end=end)
        else:
            print(i, end=end)
