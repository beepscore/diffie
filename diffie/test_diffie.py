#!/usr/bin/env python3

import unittest

# TODO: Consider move test file to a directory tests. Need to understand how Python import works!
import diffie


class TestDiffie(unittest.TestCase):

    def setUp(self):
        pass

    def test_sequence_matcher_opcodes_no_equal(self):
        actual = diffie.sequence_matcher_opcodes_no_equal('data/a.txt', 'data/b.txt')
        self.assertEqual(len(actual), 10)

if __name__ == "__main__":
    unittest.main()
