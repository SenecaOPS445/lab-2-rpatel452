#!/usr/bin/env python3
# Author: Rohan Patel
# Author ID: 154338222
# Date Created: 2024/05/23


import sys

# Check if a command line argument was provided
if len(sys.argv) > 1:
    # If an argument was provided, use it for the timer
    timer = int(sys.argv[1])
else:
    # If no argument was provided, set timer to 3 by default
    timer = 3

# Loop until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")