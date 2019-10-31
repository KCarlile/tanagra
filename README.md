# PRJECT CODENAME: tanagra
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

### Structure
The functional structure of a book is as follows:
- Content
  - Part
    - Chapter
  - Collateral (Uncertain)

You can name parts and chapters anything you want, but they will be compiled in alpha-numerical order, so you may wish to prefix with numbers.

(The following needs correction/updating.)
The following is an example of the structure of a book:
- content/
  - 00_intro/
    - 00_title.md
    - 01_dedication.md
    - 02_table_of_contents.md
    - 03_preface.md
  - 01_part_1/
    - 01_chapter_1.md
    - 02_chapter_2.md
    - 03_chapter_3.md
  - 02_part_2/
    - 01_chapter_4.md
    - 02_chapter_5.md
- media/
  - 00_intro/
    - 00_title/
      - title.jpg
    - 03_preface/
      - img_1.jpg
      - img_2.jpg
  - 01_part_1/
    - 01_chapter_1/
      - img_3.jpg
    - 02_chapter_2/
      - img_4.jpg
    - 03_chapter_3/
      - img_5.jpg
  - 02_part_2/
    - 01_chapter_4/
      - img_6.jpg
    - 02_chapter_5/
      - img_7.jpg

## content/ and media/ Directories
As seen in the structure example above, the `content/` directory contains all the Markdown text files (`*.md`) and the `media/` directory contains all local assets, such as images, in a similar structure as the `content/` directory.

### Commands
To build your book, from the root of your book (same level as the compile symobolic link), run:
```bash
./compile format
```

...where format is one of the following:
- pdf
- html
- epub

## Scripts Directory
The scripts directory should not be modified or you may break book compilation.
