#!/usr/bin/env python3

from diffie import diffie
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# if __name__ == '__main__':

print('difflib_ndiff')
#pprint.pprint(diffie.difflib_ndiff('data/input/a.txt', 'data/input/ac.txt'))

print('pieces')
# pieces = diffie.pieces('data/input/a.txt', 'data/input/ac.txt')
# for pair in pieces:
#     print(pair[0])
#     print(pair[1])
#     print()

diffie.get_diffs_write('data/input', 'data/output', 'results.txt')
