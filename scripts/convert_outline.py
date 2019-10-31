#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import re
import shutil

from os import path

BASE_FOLDER = 'content-structure'
DEFAULT_OUTLINE_FILE = 'outline.md'
DEFAULT_CONTENT_DIR = 'new_book/'

#print('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
#print('Argument List:' + str(sys.argv))

#cwd = os.getcwd()
#print('Current directory ' + cwd)

# check for arguments or ask for input
if len(sys.argv) == 3:
  outline_file = str(sys.argv[1])
  content_dir = str(sys.argv[2])
else:
  print('What is the name of your outline file? [outline_file.md]')
  outline_file = str(raw_input())
  if not outline_file:
    outline_file = DEFAULT_OUTLINE_FILE
  
  print('What is the name of your content directory? (Existing directories will be deleted.) [new_book/]')
  content_dir = str(raw_input())
  if not content_dir:
    content_dir = DEFAULT_CONTENT_DIR

print('Outline file: ' + outline_file)
print('Content directory: ' + content_dir)



# make sure outline file exists
print('Loading ' + outline_file + '...')
if path.exists(outline_file):
  print('Reading ' + outline_file + '...')
else:
  print(outline_file + ' does not exist.')
  sys.exit(1)

#with open(outline_file, 'r') as content_file:
#    content = content_file.read().replace('  ', "\t")

# read the outline file
with open(outline_file) as f:
  content = f.readlines()

structure = []

# build up structure list with valid lines
for line in content:
  # only grab the line if it starts with markdown list item 1. XXXX
  if line.lstrip(' ')[0:3] == '1. ':
    structure.append(line.strip('\n'))

# clean out the content structure
if os.path.isdir(content_dir):
  for file in os.listdir(content_dir):
    file_path = os.path.join(content_dir, file)
    try:
      if os.path.isfile(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
    except Exception as e:
      print(e)

  print(content_dir + ' emptied.')

depth = 0
part = ''
chapter = ''
section = ''
subsection = ''

outline = []


for item in structure:
  if item:
    depth = (len(item) - len(item.lstrip(' '))) / 2
    item = item.lstrip(' ').lstrip('1. ')
    #print depth, '::', item

    if depth == 0:
      # Part
      part = content_dir + '/' + item
      if not os.path.exists(part):
        os.makedirs(part)
        print(part)
    if depth == 1:
      # Chapter
      chapter = part + '/' + item + '.md'
      print(chapter)

      mode = 'a+' if os.path.exists(chapter) else 'w+'
      with open(chapter, mode) as file:
        file.write('# ' + item + "\n\n")
    if depth == 2:
      # Section
      section = '## ' + item
      print(section)

      mode = 'a+' if os.path.exists(chapter) else 'w+'
      with open(chapter, mode) as file:
        file.write('## ' + item + "\n\n\n")
    if depth == 3:
      # Subsection
      subsection = '### ' + item
      print(subsection)

      mode = 'a+' if os.path.exists(chapter) else 'w+'
      with open(chapter, mode) as file:
        file.write('### ' + item + "\n\n\n")
