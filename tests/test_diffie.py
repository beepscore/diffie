#!/usr/bin/env python3

import unittest
import pprint

# relative import didn't work
from diffie import diffie


class TestDiffie(unittest.TestCase):

    def setUp(self):
        self.input_dir_slash = './data/input/test/'

    def test_string_from_file(self):
        actual = diffie.string_from_file(self.input_dir_slash + 'a.txt')
        expected = """foo bar bas period x y z a
bar dog cat fly period a b c d3
foo
fud spaghetti wif cheese
ging fudoogab
now you see moog now you don't
"""
        self.assertEqual(actual, expected)

    def test_sequence_matcher_opcodes_no_equal(self):
        actual = diffie.sequence_matcher_opcodes_no_equal(self.input_dir_slash + 'b.txt', self.input_dir_slash + 'c.txt')
        self.assertEqual(len(actual), 6)
        expected = ["insert    a[7:7] --> b[7:8]       '' --> ' '",
                    "replace   a[8:9] --> b[9:10]      'i' --> 'e'",
                    "replace   a[53:55] --> b[54:59]     ' c' --> 'eesee'",
                    "replace   a[81:82] --> b[85:86]      's' --> 'c'",
                    "replace   a[112:113] --> b[116:117]      'o' --> 'u'",
                    "insert    a[115:115] --> b[119:120]       '' --> 'e'"]
        self.assertEqual(actual, expected)

    def test_start_index(self):
        self.assertEqual(diffie.start_index(0), 0)
        self.assertEqual(diffie.start_index(19), 0)
        self.assertEqual(diffie.start_index(20), 0)
        self.assertEqual(diffie.start_index(21), 1)
        self.assertEqual(diffie.start_index(22), 2)

    def test_end_index(self):
        self.assertEqual(diffie.end_index(0, 'abcdefghijklmnopqrstuvwxyz'), 20)
        self.assertEqual(diffie.end_index(1, 'abcdefghijklmnopqrstuvwxyz'), 21)

        self.assertEqual(diffie.end_index(4, 'abcdefghijklmnopqrstuvwxyz'), 24)
        self.assertEqual(diffie.end_index(5, 'abcdefghijklmnopqrstuvwxyz'), 25)
        self.assertEqual(diffie.end_index(6, 'abcdefghijklmnopqrstuvwxyz'), 25)
        self.assertEqual(diffie.end_index(7, 'abcdefghijklmnopqrstuvwxyz'), 25)

    def test_opcode_indexes_a(self):
        actual = diffie.opcode_indexes_a(self.input_dir_slash + 'a.txt', self.input_dir_slash + 'b.txt')
        self.assertEqual(actual, [(7, 7), (21, 21), (22, 24), (31, 35), (38, 38), (43, 47), (48, 49), (76, 80), (114, 115), (117, 118)])

    def test_opcode_indexes_b(self):
        actual = diffie.opcode_indexes_b(self.input_dir_slash + 'a.txt', self.input_dir_slash + 'b.txt')
        self.assertEqual(actual, [(7, 10), (24, 26), (27, 27), (34, 34), (37, 39), (44, 45), (46, 49), (76, 76), (110, 112), (114, 115)])

    def test_pieces_string_a(self):
        actual = diffie.pieces_string_a(self.input_dir_slash + 'a.txt', self.input_dir_slash + 'b.txt')
        expected = ['foo bar bas period x y z a\n',
                    'oo bar bas period x y z a\nbar dog cat fl',
                    'o bar bas period x y z a\nbar dog cat fly p',
                    ' period x y z a\nbar dog cat fly period a b c',
                    ' x y z a\nbar dog cat fly period a b c d3',
                    'z a\nbar dog cat fly period a b c d3\nfoo\nfud ',
                    'ar dog cat fly period a b c d3\nfoo\nfud sp',
                    'd3\nfoo\nfud spaghetti wif cheese\nging fudooga',
                    "udoogab\nnow you see moog now you don't",
                    "ogab\nnow you see moog now you don't"]

        self.assertEqual(actual, expected)

    def test_pieces_string_b(self):
        actual = diffie.pieces_string_b(self.input_dir_slash + 'a.txt', self.input_dir_slash + 'b.txt')
        expected = ['foo barbie bas period x z y a\n',
                    'barbie bas period x z y a\nbar catty fly co',
                    'bie bas period x z y a\nbar catty fly col',
                    ' period x z y a\nbar catty fly colon a b ',
                    'riod x z y a\nbar catty fly colon a b c d3\n',
                    'z y a\nbar catty fly colon a b c d3\nfoo\nfu',
                    'y a\nbar catty fly colon a b c d3\nfoo\nfud sp',
                    'd3\nfoo\nfud spaghetti cheese\nging fudooga',
                    "udoogab\nnow you see floop now you don't",
                    "gab\nnow you see floop now you don't"]
        self.assertEqual(actual, expected)

    def test_pieces(self):
        actual = diffie.pieces(self.input_dir_slash + 'a.txt', self.input_dir_slash + 'b.txt')
        expected = [('foo bar bas period x y z a\n', 'foo barbie bas period x z y a\n'),
                    ('oo bar bas period x y z a\nbar dog cat fl', 'barbie bas period x z y a\nbar catty fly co'),
                    ('o bar bas period x y z a\nbar dog cat fly p', 'bie bas period x z y a\nbar catty fly col'),
                    (' period x y z a\nbar dog cat fly period a b c', ' period x z y a\nbar catty fly colon a b '),
                    (' x y z a\nbar dog cat fly period a b c d3', 'riod x z y a\nbar catty fly colon a b c d3\n'),
                    ('z a\nbar dog cat fly period a b c d3\nfoo\nfud ', 'z y a\nbar catty fly colon a b c d3\nfoo\nfu'),
                    ('ar dog cat fly period a b c d3\nfoo\nfud sp', 'y a\nbar catty fly colon a b c d3\nfoo\nfud sp'),
                    ('d3\nfoo\nfud spaghetti wif cheese\nging fudooga', 'd3\nfoo\nfud spaghetti cheese\nging fudooga'),
                    ("udoogab\nnow you see moog now you don't", "udoogab\nnow you see floop now you don't"),
                    ("ogab\nnow you see moog now you don't", "gab\nnow you see floop now you don't")]

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
