#!/usr/bin/env python3

import time, random
n = random.randint(1, 10) * 100
n = 1000
# Get current time
start = time.time()

# Do some work
print("Sleeping for {} ms".format(n))
time.sleep(n/1000)

# Compute time between start and now
print(time.time() - start)
