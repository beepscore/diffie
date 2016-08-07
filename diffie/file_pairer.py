#!/usr/bin/env python3

import os
from diffie import file_helper


""" Utility methods for working with files and directories

http://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
https://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
"""


def file_pairs(search_dir, ignored_regex_objects):
    """
    Searches search_dir for files with similar names

    Ignores symlinks. Doesn't ignore alias.
    http://apple.stackexchange.com/questions/2991/whats-the-difference-between-alias-and-link

    param ignored_regex_objects contains regular expression objects compiled from patterns
    return list of pairs in search_dir, relative to search_dir
    """

    files_in_dir = file_helper.files_in_dir(search_dir, ignored_regex_objects)

    pairs = {}
    for filename in files_in_dir:
        # http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python#541394
        basename, file_extension = os.path.splitext(filename)
        proposed_matching_filename = basename + "c" + file_extension
        if proposed_matching_filename in files_in_dir:
            pairs[filename] = proposed_matching_filename

    return pairs
