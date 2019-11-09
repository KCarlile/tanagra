# User Instructions
The following instructions are calling the various commands for building a book using the Tanagra main script.

There are two ways to run the commands: via the Tanagra main program or [by calling each script individually](scripting-instructions.md). The purpose of the script approach is to allow for easier scripting by end users who want to automate their book's build. Similarly, each script can be called by passing arguments to it or through interactive mode in which the script asks for inputs.

## Generate a book template
**#TODO:** _Needs documentation._

## Convert an outline into a directory and file structure
Call the Tanagra main program by passing the command (convert) and you will be prompted for the outline file and the build directory:
```bash
$ tanagra convert
```

Optionally, you can include the outline file (outline.md) and the build directory (new_book/):
```bash
$ tanagra convert outline.md new_book/
```

## To compile markdown into a book... (Needs updating)
**#TODO:** _Needs documentation._
