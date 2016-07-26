#!/usr/bin/env python3

import unittest
import pprint

# TODO: Consider move test file to a directory tests. Need to understand how Python import works!
import diffie


class TestDiffie(unittest.TestCase):

    def setUp(self):
        pass

    def test_sequence_matcher_opcodes_no_equal(self):
        actual = diffie.sequence_matcher_opcodes_no_equal('data/a.txt', 'data/b.txt')
        self.assertEqual(len(actual), 10)

    def test_start_indexes_a(self):
        actual = diffie.start_indexes_a('data/a.txt', 'data/b.txt')
        self.assertEqual(actual, [7, 21, 22, 31, 38, 43, 48, 76, 114, 117])

if __name__ == "__main__":
    unittest.main()
