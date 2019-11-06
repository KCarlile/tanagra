#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import re
import shutil
import json

from os import path

BASE_FOLDER = 'content-structure'
DEFAULT_OUTLINE_FILE = 'outline.md'
DEFAULT_CONTENT_DIR = 'new_book/'

# initialize variables
param1 = None
param2 = None


def build_template():
    global parm1


def build_template_init(p_param1, p_param2):
    global param1
    global param2

    param1 = p_param1
    param2 = p_param2


def build_template_prompt():
    global param1
    global param2

    print('What is the name of your outline file? [outline_file.md]')
    outline_file = str(raw_input())
    if not outline_file:
        outline_file = DEFAULT_OUTLINE_FILE

    print(
        'What is the name of your content directory? (Existing directories will be deleted.) [new_book/]')
    content_dir = str(raw_input())
    if not content_dir:
        content_dir = DEFAULT_CONTENT_DIR


def main():
    global param1
    global param2
    # rint('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
    # print('Argument List:' + str(sys.argv))

    # cwd = os.getcwd()
    # print('Current directory ' + cwd)

    # check for arguments or ask for input
    if len(sys.argv) == 3:
        param1 = str(sys.argv[1])
        param2 = str(sys.argv[2])
    else:
        build_template_prompt()

    build_template()


if __name__ == "__main__":
    main()
