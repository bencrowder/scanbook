"""
Command-line functionality for Scanbook.
"""
import subprocess

import cv2
from skimage.filters import threshold_local


def process(filename, folder, threshold=19):
    """
    Processes an image file and saves the processed image to the specified
    folder.
    """
    image = cv2.imread(filename)

    # Convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold it
    T = threshold_local(image, threshold, offset=10, method='gaussian')
    image = (image > T).astype('uint8') * 255

    # Slightly blur it
    gaussian = cv2.GaussianBlur(image, (9, 9), 0.0)

    # Sharpen it
    image = cv2.addWeighted(image, 1.5, gaussian, -0.5, 0, image)

    # # And blur it again
    image = cv2.GaussianBlur(image, (3, 3), 10.0)

    # Resize it to 2500px high
    height = 2500
    scale_factor = height / image.shape[0]
    width = int(scale_factor * image.shape[1])
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

    cv2.imwrite(f'{folder}/{filename}', image)


def make_pdf(folder, bookname, verbose):
    """
    Converts the image files in folder to a PDF named bookname.PDF.
    """
    cmd = ['convert']

    if verbose:
        cmd.append('-verbose')

    cmd.extend([
        f'{folder}/*',
        '-compress',
        'jpeg',
        '-quality',
        '75',
        f'{bookname}.pdf',
    ])

    subprocess.run(cmd)
