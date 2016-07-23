#!/usr/bin/env python3

import difflib
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':


    def differ_compare(filename_a, filename_b):
        """
        returns differences between two files
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

pprint.pprint(differ_compare('data/a.txt', 'data/b.txt'))

