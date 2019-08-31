# Scanbook

A Python command-line tool for turning page scans into a nice black-and-white PDF.


## Installation

`python setup.py`

And make sure the Python binary path is in your $PATH.

### Dependencies

- `click`
- `opencv-python`
- `scikit-image`
- Imagemagick (`convert`)


## Usage

`scanbook BOOKNAME FILENAMES...`

Example: `scanbook war-and-peace *.jpg`

Options:

- `--threshold NUM` -- set the threshold value, if the images are turning out too light or too dark; must be an odd number (default: 19)
- `--no-cleanup` -- leave the `__BOOKNAME` folder (handy if you want to do anything with the processed image files)
- `--verbose`

Example: `scanbook --verbose --threshold 27 --no-cleanup war-and-peace *.jpg`
