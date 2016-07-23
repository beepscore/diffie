#!/usr/bin/env python3

import difflib
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':


    def differ_compare(filename_a, filename_b):
        """
        returns differences between two files using Differ.compare
        https://docs.python.org/3/library/difflib.html
        """

        lines_a = []
        lines_b = []

        with open(filename_a) as file_a:
            lines_a = file_a.readlines()

        with open(filename_b) as file_b:
            lines_b = file_b.readlines()

        differ = difflib.Differ()
        result = list(differ.compare(lines_a, lines_b))
        return result

    def difflib_ndiff(filename_a, filename_b):
        """
        returns differences between two files using difflib_ndiff
        https://docs.python.org/3/library/difflib.html
        """

        lines_a = []
        lines_b = []

        with open(filename_a) as file_a:
            lines_a = file_a.readlines()

        with open(filename_b) as file_b:
            lines_b = file_b.readlines()

        result = list(difflib.ndiff(lines_a, lines_b))
        return result

    def difflib_unified_diff(filename_a, filename_b):
        """
        returns differences between two files using difflib_unified_diff
        https://docs.python.org/3/library/difflib.html
        """

        lines_a = []
        lines_b = []

        with open(filename_a) as file_a:
            lines_a = file_a.readlines()

        with open(filename_b) as file_b:
            lines_b = file_b.readlines()

        result = list(difflib.unified_diff(lines_a, lines_b))
        return result

print('differ_compare')
pprint.pprint(differ_compare('data/a.txt', 'data/b.txt'))

print()
print('difflib_ndiff')
pprint.pprint(difflib_ndiff('data/a.txt', 'data/b.txt'))

print()
print('difflib_unified_diff')
pprint.pprint(difflib_unified_diff('data/a.txt', 'data/b.txt'))
