#!/usr/bin/env python3

"""
This is a sample Python script to demonstrate
how to use Pyflakes.
Run `pyflakes 5_crash.py`
"""
import time

def sum(a, b):
    return a + b
def num():
    print("Num num")

# There is an error below. 
# num is already defined as a function.
for num in range(5):
    print(sum(num, num+1))

tmp = 1
tmp *= 0.2

time.sleep(60)

# There is another error below.
# It should be tmp, not temp.
print(temp)

