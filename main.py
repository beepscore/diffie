#!/usr/bin/env python3

from diffie.diffie import *
import pprint

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
#if __name__ == '__main__':

print('difflib_ndiff')
pprint.pprint(difflib_ndiff('data/a.txt', 'data/b.txt'))

print('pieces')
pprint.pprint(pieces('data/a.txt', 'data/b.txt'))
