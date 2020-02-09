#!/usr/local/bin/python3
# Written for Python 3.7.5+

import sys
import os
import os.path
import re
import shutil
import logging

from os import path
from datetime import datetime
from initialize import *

DEFAULT_BOOK_NAME = 'new_book_' + datetime.today().strftime('%Y%m%d-%H%M%S')
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

# initialize variables
book_name = None


def build_template():
    global book_name

    # create book directory
    book_path = cwd + '/' + book_name

    try:
        if not os.path.exists(book_path):
            os.makedirs(book_path)
    except OSError:
        sys.exit('Book directory "' + book_path +
                 '" does not exist and cannot be created')

    # create content path
    content_path = book_path + '/content'

    try:
        # create content directory
        if not os.path.exists(content_path):
            os.makedirs(content_path)
    except OSError:
        sys.exit('Content directory "' + content_path +
                 '" does not exist and cannot be created')

    # create output path
    output_path = book_path + '/output'

    try:
        # create content directory
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except OSError:
        sys.exit('Output directory "' + output_path +
                 '" does not exist and cannot be created')

    # copy template files
    try:
        # copy outline.md
        shutil.copy(
            SCRIPT_PATH + '/templates/outline.md', book_path + '/outline.md')

        # copy metadata.md
        shutil.copy(
            SCRIPT_PATH + '/templates/metadata.md', book_path + '/metadata.md')
    except OSError:
        sys.exit('Template file copy failed.')

    logging.print_info('Template creation completed.')
    logging.print_info(content_path)
    logging.print_info(output_path)
    logging.print_info(book_path + '/metadata.md')
    logging.print_info(book_path + '/outlne.md')
    print('\n')
    logging.print_info(
        'Your book template is now ready. You may populate your metadata.md and outline.md files.')


def build_template_init(p_book_name):
    global book_name
    book_name = cleanup_book_name(p_book_name)


def build_template_prompt():
    global book_name

    logging.print_info('What is a short name for your book project? This is not your title. [' +
                       DEFAULT_BOOK_NAME + ']')
    book_name = str(input())

    if not book_name:
        book_name = DEFAULT_BOOK_NAME

    book_name = cleanup_book_name(book_name)


def cleanup_book_name(book_name):
    # make book_name a machine name string for directories
    book_name = book_name.lower().replace(' ', '_')
    book_name = re.sub('[^A-Za-z0-9_]+', '', book_name)

    return book_name


def main():
    build_template_prompt()
    build_template()


if __name__ == "__main__":
    main()
