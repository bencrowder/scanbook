"""
Command-line functionality for Scanbook.
"""
import os
import subprocess

import click
import scanbook


@click.command()
@click.argument('bookname', nargs=1)
@click.argument('filenames', nargs=-1)
@click.option('--no-cleanup', nargs=1, default=False, is_flag=True, help='Whether to leave the processed image files')
@click.option('--threshold', nargs=1, default=19, help='Threshold value, must be odd')
@click.option('--verbose', nargs=1, default=False, is_flag=True)
def main(bookname, filenames, threshold, no_cleanup, verbose):
    """
    Processes image files and turns them into a black-and-white PDF for easy
    reading. BOOKNAME is used to name the output PDF.

    Examples:

        scanbook war-and-peace *.jpg

        scanbook --threshold 27 war-and-peace *.jpg

        scanbook --no-cleanup --verbose --threshold 9 war-and-peace *.jpg
    """
    folder = f'__{bookname}'

    # Make sure the output folder exists
    if not os.path.exists(folder):
        if verbose:
            click.echo(f'Folder {folder} doesn\'t exist, creating it')
        os.makedirs(folder)

    # Process the images
    for file in filenames:
        if verbose:
            click.echo(f'Processing {file}')
        scanbook.process(file, folder, threshold)

    # Convert them to PDF
    if verbose:
        click.echo(f'Converting to PDF')
    scanbook.make_pdf(folder, bookname, verbose)

    # And clean up
    if not no_cleanup:
        if verbose:
            click.echo(f'Removing {folder}/')
        subprocess.run(['rm', '-rf', f'{folder}/'])


if __name__ == '__main__':
    main()
