# Scanbook

A Python command-line tool for turning page scans into a nice black-and-white PDF.


## Installation

`python setup.py`

### Dependencies

- `click`
- `opencv-python`
- `scikit-image`
- Imagemagick (`convert`)


## Usage

`scanbook SLUG FILES...`

Example: `scanbook war-and-peace *.jpg`

Options:

- `--threshold NUM` -- set the threshold value, if the images are turning out too light or too dark; must be an odd number (default: 19)
- `--no-cleanup` -- leave the `__SLUG` folder (handy if you want to do anything with the processed image files)

Example: `scanbook --threshold 27 --no-cleanup war-and-peace *.jpg
