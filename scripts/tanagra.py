#!/usr/local/bin/python3
# Written for Python 3.7.5+
# !/usr/bin/python
import sys
import os
import os.path
import logging

from initialize import *


# initialize variables
script = None
command = None
args = None


# welcome
# build
# check for existing project
# if yes
# exit
# else make project
# convert
# check for existing project
# if no
# exit
# if already converted (content folder not empty)
# type yes to override
# otherwise
# exit

# convert

# compile
#

# check for existing project
# if no
# make project?
# exit
# else


def main():
    global script
    global command
    global args

    script = str(sys.argv.pop(0))  # get 0

    # Welcome
    logging.print_welcome()

    # Get the intended command
    command = get_command()

    # Look for project in cwd
    cwd_result = check_current_directory()

    if cwd_result is False:
        exit(0)
    else:
        logging.print_info('Tanagra project found.')
        print('')

    # Execute specified command
    if command == Command.BUILD:
        print('Building book template.')
        build_template()
    elif command == Command.CONVERT:
        print('Converting outline into file structure.')
        convert_outline()
    elif command == Command.COMPILE:
        print('Compiling markdown into book.')
        compile_book()
    else:
        print('Command selection failed for: ' + command)


def build_template():
    global args

    import build_template

    if len(args) == 2:
        book_name = str(args[0])
        book_dir = str(args[1])
        build_template.build_template_init(book_name, book_dir)
    else:
        build_template.build_template_prompt()

    build_template.build_template()


def convert_outline():
    import convert_outline

    convert_outline.convert_outline()


def compile_book():
    global args
    import compile_book

    if len(args) == 3:
        source_dir = str(args[0])
        output_dir = str(args[1])
        output_format = str(args[2])
        compile_book.compile_book_init(source_dir, output_dir, output_format)
    else:
        compile_book.compile_book_prompt()

    compile_book.compile_book()


def check_current_directory():
    global command
    result = False

    logging.print_info(
        'Checking current working directory (' + cwd + ') for project...')

    metadata_found = os.path.exists(metadata_path)
    outline_found = os.path.exists(outline_path)
    content_found = os.path.exists(content_path)
    output_found = os.path.exists(output_path)

    if ((metadata_found is False) and (outline_found is False) and
            (metadata_found is False) and (outline_found is False)):
        logging.print_warning(
            'Tanagra project not found in current directory: ' + cwd)
        logging.print_info(
            'Would you like to create a new project in this directory? [yes]')

        command_choice = str(input())

        if (not command_choice) or (command_choice == 'yes'):
            result = True
            global command
            command = Command.BUILD
        print('')
    elif ((metadata_found is False) or (outline_found is False) or
            (metadata_found is False) or (outline_found is False)):
            # project not properly initialized
        logging.print_error('Tanagra project not properly initialized.')

        if metadata_found is False:
            logging.print_error('  - metadata.md file not found.')

        if outline_found is False:
            logging.print_error('  - outline.md file not found.')

        if content_found is False:
            logging.print_error('  - content/ directory not found.')

        if output_found is False:
            logging.print_error('  - output/ directory not found.')

        logging.print_warning(
            'Please run Tanagra to build new book template or attempt to resolve issues.')
        print('')
    else:
        result = True

    return result


def get_command():
    global command
    global args

    if len(sys.argv) > 0:
        # get the command argument (build, convert, compile)
        command_arg = str(sys.argv.pop(0)).lower()  # get 1

        if command_arg == 'build':
            command = Command.BUILD
        elif command_arg == 'convert':
            command = Command.CONVERT
        elif command_arg == 'compile':
            command = Command.COMPILE
        else:
            print_error('Command arugment is not valid.')
            exit(1)

        args = sys.argv  # get arguments
    else:
        # command argument not provided
        print('Please enter a number to specify a command.')
        print(' [1] Build a new book template')
        print(' [2] Convert outline into file structure')
        print(' [3] Compile markdown files and media into a book')
        print(' [4] Exit Tanagra')
        command_choice = str(input())
        args = []  # make args list empty set as there have been none provided

        if not command_choice:
            print('Failed to enter a command selection.')
            exit(1)
        elif command_choice == '1':
            command = Command.BUILD
        elif command_choice == '2':
            command = Command.CONVERT
        elif command_choice == '3':
            command = Command.COMPILE
        elif command_choice == '4':
            sys.exit(0)
        else:
            print('Failed to enter a valid command selection.')
            exit(1)


if __name__ == "__main__":
    main()
