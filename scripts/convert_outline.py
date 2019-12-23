#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import shutil

from os import path
from initialize import *


def convert_outline():
    print('Content directory: ' + content_path)
    print('Outline file: ' + output_path)

    # make sure outline file exists
    print('Loading ' + outline_path + '...')
    if path.exists(outline_path):
        print('Reading ' + outline_path + '...')
    else:
        print(outline_path + ' does not exist.')
        sys.exit(1)

    # read the outline file
    with open(outline_path) as f:
        content = f.readlines()

    structure = []

    # build up structure list with valid lines
    for line in content:
        # only grab the line if it starts with markdown list item 1. XXXX
        if line.lstrip(' ')[0:3] == '1. ':
            structure.append(line.strip('\n'))

    # clean out the content structure
    if os.path.isdir(content_path):
        for file in os.listdir(content_path):
            file_path = os.path.join(content_path, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)

        print(content_path + ' emptied.')

    depth = 0
    part = ''
    chapter = ''
    section = ''
    subsection = ''

    for item in structure:
        if item:
            depth = (len(item) - len(item.lstrip(' '))) / 2
            item = item.lstrip(' ').lstrip('1. ')

            if depth == 0:
                # Part
                part = content_path + '/' + item
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


def main():
    convert_outline()


if __name__ == "__main__":
    main()
