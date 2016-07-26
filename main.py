#!/usr/bin/env python3

from diffie.diffie import *
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
#if __name__ == '__main__':

print('differ_compare')
pprint.pprint(differ_compare('data/a.txt', 'data/b.txt'))

print()
print('difflib_ndiff')
pprint.pprint(difflib_ndiff('data/a.txt', 'data/b.txt'))

print()
print('difflib_unified_diff')
pprint.pprint(difflib_unified_diff('data/a.txt', 'data/b.txt'))

print()
print('sequence_matcher_opcodes')
pprint.pprint(sequence_matcher_opcodes('data/a.txt', 'data/b.txt'))

print()
print('sequence_matcher_opcodes_no_equal')
pprint.pprint(sequence_matcher_opcodes_no_equal('data/b.txt', 'data/c.txt'))
