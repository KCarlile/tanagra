#!/usr/bin/python
# Written for Python 2.7.10

import sys
import os
import os.path
import logging

# initialize variables
script = None
command = None
args = None


def main():
    logging.print_welcome()
    cwd_result = check_current_directory()

    if cwd_result is False:
        exit(0)

    global script
    global command
    global args

    script = str(sys.argv.pop(0))  # get 0

    if len(sys.argv) > 0:
        command = str(sys.argv.pop(0)).lower()  # get 1
    else:
        command = None

    args = sys.argv  # get arguments

    if not command:
        print('Please enter a number to specify a command.')
        print(' [1] Build new book template')
        print(' [2] Convert outline into file structure')
        print(' [3] Compile markdown files and media into a book')
        print(' [4] Exit Tanagra')
        command_choice = str(raw_input())
        args = []  # make args list empty set as there

        if not command_choice:
            print('Failed to enter a command selection.')
            exit(1)
        elif command_choice == '1':
            command = 'build'
        elif command_choice == '2':
            command = 'convert'
        elif command_choice == '3':
            command = 'compile'
        elif command_choice == '4':
            sys.exit(0)
        else:
            print('Failed to enter a valid command selection.')
            exit(1)

    if command == 'build':
        print('Build book template.')
        build_template()
    elif command == 'convert':
        print('Convert outline to file structure...')
        convert_outline()
    elif command == 'compile':
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
    global args
    import convert_outline

    if len(args) == 2:
        outline_file = str(args[0])
        content_dir = str(args[1])
        convert_outline.convert_outline_init(outline_file, content_dir)
    else:
        convert_outline.convert_outline_prompt()

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
    result = False
    cwd = os.getcwd()

    logging.print_info(
        'Checking current working directory (' + cwd + ') for project...')

    metadata_path = cwd + '/metadata.md'
    outline_path = cwd + '/outline.md'
    content_path = cwd + '/content'
    output_path = cwd + '/output'

    metadata_found = os.path.exists(metadata_path)
    outline_found = os.path.exists(outline_path)
    content_found = os.path.exists(content_path)
    output_found = os.path.exists(output_path)

    if ((metadata_found is False) and (outline_found is False) and
            (metadata_found is False) and (outline_found is False)):
        logging.print_info(
            'Tanagra project not found in current directory: ' + cwd)
        logging.print_info(
            'Would you like to create a new project in this directory? [yes]')

        command_choice = str(raw_input())

        if (not command_choice) or (command_choice == 'yes'):
            result = True
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
        logging.print_info('Tanagra project found.')
        print('')
        result = True

    return result


if __name__ == "__main__":
    main()
