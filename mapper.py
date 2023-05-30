#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the record into fields
    fields = line.split(',')
    # field 1 is the date while field 8 is Dry Bulb Temp
    print('%s,%s' % (fields[1], fields[8]))
