# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(message):
    print(bcolors.OKBLUE + message + bcolors.ENDC)


def print_info(message):
    print(bcolors.OKGREEN + message + bcolors.ENDC)


def print_warning(message):
    print(bcolors.WARNING + message + bcolors.ENDC)


def print_error(message):
    print(bcolors.FAIL + message + bcolors.ENDC)


def print_welcome():
    print_header('-------------------------------------')
    print_header('| Tanagra                           |')
    print_header('|   A markdown book pipeline tool   |')
    print_header('-------------------------------------')
    print('')
