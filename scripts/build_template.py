#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import re

from os import path

BASE_FOLDER = 'content-structure'
DEFAULT_PROJECT_NAME = 'outline.md'

#print('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
#print('Argument List:' + str(sys.argv))

#cwd = os.getcwd()
#print('Current directory ' + cwd)

# check for arguments or ask for input
if len(sys.argv) == 3:
  outline_file = str(sys.argv[1])
  content_dir = str(sys.argv[2])
else:
  print('What is the name of your project file? [outline_file.md]')
  outline_file = str(raw_input())
  if not outline_file:
    outline_file = DEFAULT_OUTLINE_FILE

print('Outline file: ' + outline_file)
print('Content directory: ' + content_dir)



# make sure outline file exists
print('Loading ' + outline_file + '...')
if path.exists(outline_file):
  print('Reading ' + outline_file + '...')
else:
  print(outline_file + ' does not exist.')
  sys.exit(1)
