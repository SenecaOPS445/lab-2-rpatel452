#!/usr/bin/env python3

import sys

# Check if the number of arguments is not exactly 2
if len(sys.argv) != 3:
    print("Usage: {} name age".format(sys.argv[0]))
    sys.exit()

# Assigning the first argument to the object "name"
name = sys.argv[1]

# Assigning the second argument to the object "age"
age = sys.argv[2]

# Print the exact output as required
print("Hi {}, you are {} years old.".format(name, age))
