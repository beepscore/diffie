#!/usr/bin/env python3

from diffie.diffie import *
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# if __name__ == '__main__':

print('difflib_ndiff')
pprint.pprint(difflib_ndiff('data/input/a.txt', 'data/input/ac.txt'))

print('pieces')
pieces = pieces('data/input/a.txt', 'data/input/ac.txt')
for pair in pieces:
    print(pair[0])
    print(pair[1])
    print()

# get_pieces_and_write('data/input/a.txt', 'data/input/ac.txt', 'data/output', 'results.txt')

get_pieces_lines_and_write('data/input/a.txt', 'data/input/ac.txt', 'data/output', 'results.txt')
