#!/usr/bin/env python3
# Author: Rohan Patel
# Author ID: 154338222
# Date Created: 2024/05/23

import sys

# Assign the value of the first command line argument to the timer variable
timer = int(sys.argv[1])

# Loop until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")