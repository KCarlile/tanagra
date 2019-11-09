# Scripting Instructions
The following instructions are for calling the individual scripts directly.

There are two ways to run the commands: [via the Tanagra main program](user-instructions.md) or by calling each script individually. The purpose of the script approach is to allow for easier scripting by end users who want to automate their book's build. Similarly, each script can be called by passing arguments to it or through interactive mode in which the script asks for inputs.

**Note: All of these commands assume that your current working directory is the tanagra project directory.**

## Generate a book template
**#TODO:** _Needs documentation._

## Convert an outline into a directory and file structure
To convert a markdown outline file into a book directory structure and files, call the `convert_outline` script and pass the outline file (`outline.md`) and the target directory to the `convert_outline` script:
```bash
$ ./scripts/convert_outline.py outline.md new_book
```

If you don't pass the parameters, the script will enter interactive mode and ask you for those values.
```bash
$ ./scripts/convert_outline.py
```

## To compile markdown into a book... (Needs updating)
**#TODO:** _Needs documentation._
