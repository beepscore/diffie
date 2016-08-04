#!/usr/bin/env python3

import os


def absolute_dir_path(dirname):
    # Note Python does not expand ~ in path as on OS X
    # http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    # current_dir is absolute path
    # current_dir = os.path.dirname(__file__)
    absolute_path = os.path.abspath(dirname)
    return absolute_path


def absolute_file_path(dirname, filename):
    dir_path = absolute_dir_path(dirname)
    file_path = os.path.join(dir_path, filename)
    return file_path


def create_directory(dirname):
    """
    Creates directory at dirname if it doesn't exist.
    """
    abs_dir_path = absolute_dir_path(dirname)
    # http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary
    try:
        os.makedirs(abs_dir_path)
    except OSError:
        if not os.path.isdir(abs_dir_path):
            raise


def filename_from_url(url):
    """
    Similar to Django slugify
    http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python

    :param url: url to convert
    :return: a valid filename
    """
    filename = "".join(i for i in url if i not in "\/:*?<>|")
    return filename


def create_file(dirname, filename, content):
    """
    Creates file at path and writes content
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    """
    abs_file_path = absolute_file_path(dirname, filename)
    create_directory(dirname)
    # https://docs.python.org/3.3/tutorial/inputoutput.html
    f = open(abs_file_path, 'w')
    f.write(content)
    f.close()

