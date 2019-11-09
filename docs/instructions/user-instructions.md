# Scripting Instructions
Instructions for Scripting (in progress)

There are two ways to run the commands: through the Tanagra main program or by calling each script individually. The purpose for these two methods is to allow for easier scripting by end users. Similarly, each script can be called by passing agruments to it or through interactive mode in which the script asks for inputs.

## Generate a book tempalte
Coming soon...

### To convert outline to directory and file structure...
Call the Tanagra main program by passing the command (convert) and you will be prompted for the outline file and the build directory:
```bash
./scripts/tanagra.py convert
```

Optionally, you can include the outline file (outline.md) and the build directory (new_book/):
```bash
./scripts/tanagra.py convert outline.md new_book/
```

### To compile markdown into a book... (Needs updating)
To build your book, from the root of your book (same level as the compile symobolic link), run:
```bash
./compile format
```

...where format is one of the following:
- pdf
- html
- epub
