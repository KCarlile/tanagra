#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import shutil
import subprocess

from os import path

import init

# initialize variables
source_dir = None
output_dir = None
output_format = None


def compile_book():
    global source_dir
    global output_dir
    global output_format

    source_dir = source_dir.rstrip('\/')
    output_dir = output_dir.rstrip('\/')

    file_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
        source_dir) for f in filenames if os.path.splitext(f)[1] == '.md']

    file_list = sorted(file_list)

    extra = ''
    output_file = str(output_dir) + '/output.' + str(output_format)

    # leave out the file list
    args = ['pandoc', '-s', '-o', str(output_file)]
    # splice in the file list to avoid Pandoc weirdness
    args[2:2] = file_list

    try:
        # run pandoc with the parameters
        subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        print e.output
        print("Pandoc converstion failed: ", str(args))

    # handle copying media over to the output directory for HTML
    # if output_format == 'html':
# if [ $FORMAT=html ]; then
#   rm -r output/media
#   cp -R media output/
# fi

    # TODO: output success mesage


def compile_book_init(p_source_dir, p_output_dir, p_output_format):
    global source_dir
    global output_dir
    global output_format

    source_dir = p_source_dir
    output_dir = p_output_dir
    output_format = p_output_format


def compile_book_prompt():
    global source_dir
    global output_dir
    global output_format

    print('What is the source directory for your book\'s markdown files?')
    source_dir = os.path.expanduser(raw_input())
    if not source_dir:
        print('Source directory not provided.')
        exit(1)
    elif not os.path.isdir(source_dir):
        print('Source directory is invalid.')
        exit(1)

    print('What is the desired output directory for your book\'s rendered file(s)?')
    output_dir = os.path.expanduser(raw_input())
    if not output_dir:
        print('Output directory not provided.')
        exit(1)

    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except OSError:
        sys.exit('Output directory "' + output_dir +
                 '" does not exist and cannot be created')

    print('Please select the output format for your rendered book. [PDF]')
    print(' [1] PDF')
    print(' [2] EPUB')
    print(' [3] HTML')
    output_format_choice = str(raw_input())

    if not output_format_choice:
        print('Failed to enter a command selection.')
        exit(1)
    elif output_format_choice == '1':
        output_format = 'pdf'
    elif output_format_choice == '2':
        output_format = 'epub'
    elif output_format_choice == '3':
        output_format = 'html'
    else:
        print('Failed to enter a valid output format selection.')
        exit(1)


def main():
    global source_dir
    global output_dir
    global output_format

    # check for arguments or ask for input
    if len(sys.argv) == 4:
        source_dir = str(sys.argv[1])
        output_dir = str(sys.argv[2])
        output_format = str(sys.argv[3])
    else:
        compile_book_prompt()

    compile_book()


if __name__ == "__main__":
    main()
