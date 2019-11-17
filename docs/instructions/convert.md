# **Convert an Outline into a Directory and File Structure**
Once your outline is complete, you can run the `convert` command to generate a directory structure and set of files based on your outline file. The convert command will create directories for parts, files for chapters, and headings within the chapter files for sections and subsections, such as:
```bash
part_1/
   ch_1.md
      ## section 1
      ## section 2
   ch_2.md
      ## section 1
      ## section 2
         ### subsection 2.1
part_2/
   ch_3.md
      ## section 1
   ch_4.md
      ## section 1
         ### subsection 1.1
      ## section 2
   ch_5.md
```

## **tagangra convert** [_outline_file_ _build_directory_]
Converts an outline markdown file _outline_file_ (optional) into a book directory and file structure in the _build_directory_ (optional) and adds section and subsection headings to chapter markdown files.


### Interactive Mode
To convert a markdown outline file into a book directory structure and files, call the Tanagra main program by passing the command (convert) and you will be prompted for the outline file and the build directory:
```bash
$ tanagra convert
```

### Command Mode
Optionally, you can include the outline file (outline.md) and the build directory (new_book/):
```bash
$ tanagra convert outline.md new_book/
```

## Next Steps
Now that your book directory and file structure has been generated, you can write your book in the `content/` directory and generated \*.md files. When your book is complete, you can [compile your markdown into a rendered book](compile.md).
