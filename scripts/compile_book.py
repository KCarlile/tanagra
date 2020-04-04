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
    copy_media_cwd()

    global output_format
    output_file_name = 'output'  # TODO: replace with book name

    file_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
        content_path) for f in filenames if os.path.splitext(f)[1] == '.md']

    file_list = sorted(file_list)

    output_format_path = str(output_path) + '/' + \
        str(output_format.value) + '/'

    try:
        cleanup_output(str(output_format.value))

        # create content directory
        if not os.path.exists(output_format_path):
            os.makedirs(output_format_path)
    except OSError:
        sys.exit('Output format directory "' + output_format_path +
                 '" does not exist and cannot be created')

    output_file = output_format_path + 'output.' + str(output_format.value)

    # leave out the file list
    if output_format.value == Format.PDF.value:
        args = ['pandoc', '--pdf-engine=xelatex', '-s', '-o', str(output_file)]
    else:
        args = ['pandoc', '-s', '-o', str(output_file)]
    # splice in the file list to avoid Pandoc weirdness
    args[2:2] = file_list

    try:
        # run pandoc with the parameters
        subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        cleanup_media()
        logging.print_error(e.output)
        logging.print_error("Pandoc converstion failed: ", str(args))

    if (output_format == Format.HTML):
        copy_media_html()

    cleanup_media()

    logging.print_info("Markdown book compiled into " +
                       str(output_format.value).upper() + ": " + output_file)


def copy_media_cwd():
    """
    Copies media folders from content/ to cwd for compilation
    """
    media_dirs = []

    for (root, dirs, files) in os.walk(content_path):
        if(root.endswith('_media')):
            media_dirs.append(root)

    # copy media folders to root
    try:
        for media_dir in media_dirs:
            dir_name = os.path.basename(os.path.normpath(media_dir))
            shutil.copytree(media_dir, cwd + '/' + dir_name)
    # except OSError:
    except OSError as err:
        logging.print_error("OS error: {0}".format(err))
        sys.exit('Media directory copy to cwd failed.')


def copy_media_html():
    """
    Copies media folders from cwd to output for HTML post compilation
    """
    media_root_dirs = []

    for child in next(os.walk(cwd))[1]:
        if(os.path.isdir(child)) and child.endswith('_media'):
            media_root_dirs.append(child)

    # copy media folders to output
    try:
        for media_dir in media_root_dirs:
            dir_name = os.path.basename(os.path.normpath(media_dir))
            shutil.copytree(media_dir, output_path + '/html/' + dir_name)
    # except OSError:
    except OSError as err:
        logging.print_error("OS error: {0}".format(err))
        sys.exit('Media directory copy to output failed.')


def cleanup_media():
    """
    Removes copies of media directories from root following compilation
    """
    media_root_dirs = []

    for child in next(os.walk(cwd))[1]:
        if(os.path.isdir(child)) and child.endswith('_media'):
            media_root_dirs.append(child)

    # cleanup media directories from root
    try:
        for media_root_dir in media_root_dirs:
            logging.print_info('Cleanup: ' + cwd + '/' + media_root_dir)
            shutil.rmtree(cwd + '/' + media_root_dir)
    # except OSError:
    except OSError as err:
        logging.print_error("OS error: {0}".format(err))
        sys.exit('Media directory cleanup failed.')


def cleanup_output(format=None):
    """
    Removes compiled output for the specified format or all output when no format is provided.

    Parameters:
        format  PDF, EPUB, or HTML; null will empty the entire output directory
    """
    # Execute specified command
    if format == Format.PDF.value:
        logging.print_info("Deleting output for PDF.")
    elif format == Format.EPUB.value:
        logging.print_info("Deleting output for EPUB.")
    elif format == Format.HTML.value:
        logging.print_info("Deleting output for HTML.")
    else:
        logging.print_info("Deleting output for all formats.")

    # cleanup output directories
    try:
        shutil.rmtree(cwd + '/output/' + format)
    # except OSError:
    except OSError as err:
        logging.print_error("OS error: {0}".format(err))
        sys.exit('Output directory cleanup failed.')


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
