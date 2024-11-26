#!/usr/bin/env python3
"""
This is a sample Python script that shows
how to print current line and file in Python.
"""
from inspect import currentframe, getframeinfo

def run():
    f = currentframe()
    line = getframeinfo(f).lineno
    print("Hello World! You’re on line {} in {}".format(line, __file__))

if __name__ == "__main__":
    run()
