#!/usr/bin/python
# Written for Python 2.7.10

import sys

# initialize variables
script = None
command = None
args = None


def main():
    global script
    global command
    global args

    #print('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
    #print('Argument List:' + str(sys.argv))

    script = str(sys.argv.pop(0))  # get 0

    if len(sys.argv) > 0:
        command = str(sys.argv.pop(0)).lower()  # get 1
    else:
        command = None

    args = sys.argv  # get arguments

    #print('Script: ' + str(script))
    #print('Command: ' + str(command))
    #print('Args: ' + str(args))

    if not command:
        print('Please enter a number to specify a command.')
        print(' [1] Build new book template')
        print(' [2] Convert outline into file structure')
        print(' [3] Compile markdown files and media into a book')
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


if __name__ == "__main__":
    main()
