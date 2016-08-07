#!/usr/bin/env python3

from diffie import diffie
from diffie import expression_helper
from diffie import file_pairer
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# if __name__ == '__main__':

print('difflib_ndiff')
pprint.pprint(diffie.difflib_ndiff('data/input/a.txt', 'data/input/ac.txt'))

print('pieces')
pieces = diffie.pieces('data/input/a.txt', 'data/input/ac.txt')
for pair in pieces:
    print(pair[0])
    print(pair[1])
    print()

# diffie.get_pieces_and_write('data/input/a.txt', 'data/input/ac.txt', 'data/output', 'results.txt')
# diffie.get_pieces_lines_and_write('data/input/a.txt', 'data/input/ac.txt', 'data/output', 'results.txt')

ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

file_pairs = file_pairer.file_pairs("./data/input", ignored_regex_objects)
print("file_pairs {}".format(file_pairs))

for key in file_pairs:
    print("key {}, value {}".format(key, file_pairs[key]))
    diffie.get_pieces_lines_and_write(key, file_pairs[key], 'data/input', 'data/output', 'results.txt')
