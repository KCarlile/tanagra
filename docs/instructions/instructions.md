# User Instructions
The following instructions are calling the various commands for building a book using the Tanagra main script.

There are two ways to run the commands: _Interactive Mode_ or _Command Mode_.

In _Interactive Mode_, the user supplies the least information possible to the Tanagra main program and the user is prompted to enter data when needed. **If you aren't sure which mode to use,** stick with _Interactive Mode_ as the same code is executed, but with a simpler user experience.

In _Command Mode_, the user supplies all of the necessary parameters at the time of calling the Tanagra main program. _Command Mode_ is more suitable for scripting or advanced users. Advanced users who wish to script builds may also want to [call each Tanagra sub-script individually](#calling-scripts-directly).

## **Build a Book Template**
See [Build a Book Template](build.md).

## **Convert an Outline into a Directory and File Structure**
See [Convert an Outline into a Directory and File Structure](convert.md).

## **Compile Markdown into a Rendered Book**
See [Compile Markdown into a Rendered Book](compile.md).

## Calling Scripts Directly
If you want to bypass the Tanagra main program, you can call the individual scripts directly from within the `scripts/` directory of the Tanagra installation, which is probably `/usr/local/tanagra/scripts/`. The following scripts can be called directly using the same parameters outlined in the instructions above:
- build_template.py: direct script call for `tanagra build`
- convert_outline.py: direct script call for `tanagra convert`
- compile_book.py: direct script call for `tanagra compile`
