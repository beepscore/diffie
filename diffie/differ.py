#!/usr/bin/env python3

import difflib

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':


    def differences(filename_a, filename_b):
        """
        returns differences between two files
        """

        lines_a = []

        with open(filename_a) as file_a:
            lines_a = file_a.readlines()

        return lines_a

print(differences('data/a.txt', 'data/b.txt'))

