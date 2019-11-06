#!/usr/bin/python

import sys
import os

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
    str(sys.argv[1])) for f in filenames if os.path.splitext(f)[1] == '.md']
print " ".join(sorted(result))
