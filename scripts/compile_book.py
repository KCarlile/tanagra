#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import shutil
import subprocess
import logging

from os import path
from initialize import *

# initialize variables
output_format = None


def compile_book():
    global output_format

    file_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
        content_path) for f in filenames if os.path.splitext(f)[1] == '.md']

    file_list = sorted(file_list)

    extra = ''
    output_file = str(output_path) + '/output.' + str(output_format.value)

    # leave out the file list
    args = ['pandoc', '-s', '-o', str(output_file)]
    # splice in the file list to avoid Pandoc weirdness
    args[2:2] = file_list

    try:
        # run pandoc with the parameters
        subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        logging.print_error(e.output)
        logging.print_error("Pandoc converstion failed: ", str(args))

    # handle copying media over to the output directory for HTML
    # if output_format == 'html':
# if [ $FORMAT=html ]; then
#   rm -r output/media
#   cp -R media output/
# fi

    # TODO: output success mesage


def compile_book_init(p_output_format):
    global output_format

    if p_output_format == Format.PDF.value:
        output_format = Format.PDF
    elif p_output_format == Format.EPUB.value:
        output_format = Format.EPUB
    elif p_output_format == Format.HTML.value:
        output_format = Format.HTML
    else:
        logging.print_error(
            'Invalid option for output format provided: ' + p_output_format)
        exit(1)


def compile_book_prompt():
    global output_format

    logging.print_info(
        'Please select the output format for your rendered book.')
    logging.print_info(' [1] PDF')
    logging.print_info(' [2] EPUB')
    logging.print_info(' [3] HTML')
    output_format_choice = str(input())

    if not output_format_choice:
        logging.print_error('Failed to enter a command selection.')
        exit(1)
    elif output_format_choice == '1':
        output_format = Format.PDF
    elif output_format_choice == '2':
        output_format = Format.EPUB
    elif output_format_choice == '3':
        output_format = Format.HTML
    else:
        logging.print_error('Failed to enter a valid output format selection.')
        exit(1)


def main():
    compile_book()


if __name__ == "__main__":
    main()
