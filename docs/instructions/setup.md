# Setup
## Prerequisites
- Python 2.7.10+
- Bash shell

## Installation
### Installing on Mac OS X
- Install [Homebrew](https://brew.sh/) package manager
  ```bash
  $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  ```
- Install [Pandoc](https://pandoc.org/)
   ```bash
   $ brew install pandoc
   ```
- For PDF conversion, install Mactex
   ```brew
   $ cask install mactex
   ```
   - Start a new terminal session after stalling mactex if you encounter errors generating PDFs.

- **#TODO:** _Needs documentation for installing to `/usr/local/bin/`_

### Installing on Windows
**#TODO:** _Needs documentation._

### Installing on Linux
**#TODO:** _Needs documentation._

## Writing the Book
Tanagra presumes the author is using GitHub's [markdown format](https://guides.github.com/features/mastering-markdown/) for outline conversion, although the converter mechanism is more flexible.
