#!/usr/bin/env python3

import difflib

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':


    def differences(filename_a, filename_b):
        """
        returns differences between two files
        """

        lines_a = []
        lines_b = []

        with open(filename_a) as file_a:
            lines_a = file_a.readlines()

        with open(filename_b) as file_b:
            lines_b = file_b.readlines()

        return lines_a, lines_b

print(differences('data/a.txt', 'data/b.txt'))

