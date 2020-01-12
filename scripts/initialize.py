#!/usr/local/bin/python3
# Written for Python 3.7.5+

import os

from enum import Enum

# initialize variables
cwd = os.getcwd()
metadata_path = os.path.expanduser(cwd + '/metadata.md')
outline_path = os.path.expanduser(cwd + '/outline.md')
content_path = os.path.expanduser(cwd + '/content')
output_path = os.path.expanduser(cwd + '/output')


class Command(Enum):
    """
    Enumeration (class) for valid commands
    """
    FAIL = 0
    BUILD = 1
    CONVERT = 2
    COMPILE = 3


class Format(Enum):
    """
    Enumeration (class) for falid formats
    """
    PDF = 'pdf'
    EPUB = 'epub'
    HTML = 'html'
