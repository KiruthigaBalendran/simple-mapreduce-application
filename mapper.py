#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=12:
        product = line[1]
        country = line[7]

        print(country + '\t' + product)
