#!/usr/bin/env python3
"""
This is a Python example to show how the Python debugger
works. 
"""
import pdb

def run():
    # The following is used to stop the code.
    breakpoint()

    print("Please enter a number:")
    a = input()
    print(a)

    # Another breakpoint
    breakpoint()

    print("You are in file {}".format(__file__))
    breakpoint()

if __name__ == "__main__":
    run()
