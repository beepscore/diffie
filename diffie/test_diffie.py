#!/usr/bin/env python3

import unittest
import pprint

# TODO: Consider move test file to a directory tests. Need to understand how Python import works!
import diffie


class TestDiffie(unittest.TestCase):

    def setUp(self):
        pass

    def test_string_from_file(self):
        actual = diffie.string_from_file('data/a.txt')
        expected = """foo bar bas period x y z a
bar dog cat fly period a b c d3
foo
fud spaghetti wif cheese
ging fudoogab
now you see moog now you don't
"""
        self.assertEqual(actual, expected)

    def test_sequence_matcher_opcodes_no_equal(self):
        actual = diffie.sequence_matcher_opcodes_no_equal('data/b.txt', 'data/c.txt')
        self.assertEqual(len(actual), 6)
        expected = ["insert    a[7:7] --> b[7:8]       '' --> ' '",
                "replace   a[8:9] --> b[9:10]      'i' --> 'e'",
                "replace   a[53:55] --> b[54:59]     ' c' --> 'eesee'",
                "replace   a[81:82] --> b[85:86]      's' --> 'c'",
                "replace   a[112:113] --> b[116:117]      'o' --> 'u'",
                "insert    a[115:115] --> b[119:120]       '' --> 'e'"]
        self.assertEqual(actual, expected)

    def test_start_indexes_a(self):
        actual = diffie.start_indexes_a('data/a.txt', 'data/b.txt')
        self.assertEqual(actual, [7, 21, 22, 31, 38, 43, 48, 76, 114, 117])

    def test_start_indexes_b(self):
        actual = diffie.start_indexes_b('data/a.txt', 'data/b.txt')
        self.assertEqual(actual, [7, 24, 27, 34, 37, 44, 46, 76, 110, 114])

    def test_pieces_string_a(self):
        actual = diffie.pieces_string_a('data/a.txt', 'data/b.txt')
        expected = ['',
                'r bas period x y z a\nbar dog c',
                ' bas period x y z a\nbar dog ca',
                'od x y z a\nbar dog cat fly per',
                'z a\nbar dog cat fly period a b',
                'ar dog cat fly period a b c d3',
                'g cat fly period a b c d3\nfoo\n',
                'o\nfud spaghetti wif cheese\ngin',
                'ab\nnow you see moog now you do',
                "now you see moog now you don't"]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
