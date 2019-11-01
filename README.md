# PROJECT CODENAME: tanagra
Markdown converter for generating HTML, PDF, and EPUB books.

## Writing the Book
Use GitHub's [markdown format](https://guides.github.com/features/mastering-markdown/).

## Building the Book on Mac
### Prerequisites
- Python
- Homebrew

Requires Pandoc and Mactex (PDF generation)
- `brew install pandoc`
- `brew cask install mactex`
  - Start a new terminal session after stalling mactex if you encounter errors generating PDFs.

### Structure (Needs updating)
The functional structure of a book is as follows:
1. Content
   1. Part
      1. Chapter
         1. Section
            1. Subsection
1. Media <<< Media structure TBD

You can name parts and chapters anything you want, but they will be compiled in alpha-numerical order, so you may wish to prefix with numbers.

(The following needs correction/updating.)
The following is an example of the structure of a book:

```
- book_project_name/
   - Part 0 - Part Title/
      - Chapter 1 - Chapter Title.md
         - Section Title
            - Subsection Title
      - Chapter 2 - Chapter Title.md
         - Section Title
            - Subsection Title
   - Part 1 - Part Title/
      - Chapter 3 - Chapter Title.md
         - Section Title
            - Subsection Title
      - Chapter 4 - Chapter Title.md
         - Section Title
            - Subsection Title
- media/ <<< Media structure TBD
```

## content/ and media/ Directories (Needs updating)
As seen in the structure example above, the `content/` directory contains all the Markdown text files (`*.md`) and the `media/` directory contains all local assets, such as images, in a similar structure as the `content/` directory.


## Scripts Directory
The scripts directory should not be modified or you may break Tanagra functionality.


## Instructions (in progress)

There are two ways to run the commands: through the Tanagra main program or by calling each script individually. The purpose for these two methods is to allow for easier scripting by end users. Similarly, each script can be called by passing agruments to it or through interactive mode in which the script asks for inputs.

### To build a book template...
Coming soon...

### To convert outline to directory and file structure...
Call from the Tanagra main program by passing the command (convert) and you will be prompted for the outline file and the build directory:
```bash
./scripts/tanagra.py convert
```

Optionally, you can include the outline file (outline.md) and the build directory (new_book/):
```bash
./scripts/tanagra.py convert outline.md new_book/
```

Similarly, you can also call the script directly with or without parameters:
```bash
./scripts/convert_outline.py
```

```bash
./scripts/convert_outline.py outline.md new_book
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
