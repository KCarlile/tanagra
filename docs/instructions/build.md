# **Build a Book Template**
A book template includes a book directory with the following:
- content directory: this will contain your book's content
- output directory: this will contain your book's rendered files (PDF, EPUB, HTML)
- outline markdown file: your book's outline used for generating file and directory structure
- metadata markdown file: information about your book

## **tagangra build** [_book_name_ _build_directory_]
Generates a book directory with the name _book_name_ (optional) in the specified build directory (optional). Within the newly created book directory, `content/` and `output/` directories will be created. In addition, an outline markdown file (`outline.md`) and a metadata file (`metadata.md`) will be created in the root of the new book directory.

### Interactive Mode
Call the Tanagra main program by passing the `build` command and you will be prompted for the book name and desired book directory:
```bash
$ tanagra build
```

### Command Mode
Optionally, you can include the book name (`book_name`) and the build directory (`build_directory/`):
```bash
$ tanagra build book_name build_directory/
```

## Next Steps
Now that your book template has been generated, you can populate your `metadata.md` and `outline.md` files. Once those are complete, you can [convert your outline to a book template](convert.md).
