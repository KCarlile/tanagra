# Scripting Instructions
Instructions for Scripting (in progress)

## Generate a book tempalte
Coming soon...

## Convert an outline into a directory and file structure
To convert a markdown outline file into a book directory structure and files, call the `convert_outline` script.

Pass the markdown outline file and the target directory to the `convert_outline` script:
```bash
./scripts/convert_outline.py outline.md new_book
```

## To compile markdown into a book... (Needs updating)
To build your book, from the root of your book (same level as the compile symobolic link), run:
```bash
./compile format
```

...where format is one of the following:
- pdf
- html
- epub
