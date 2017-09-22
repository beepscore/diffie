#!/usr/bin/env python3

import unittest
from diffie import file_pairer
from diffie import expression_helper


class TestFilePairer(unittest.TestCase):

    def setUp(self):
        self.input_dir_slash = './data/input/test/'

    def test_file_pairs(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_pairer.file_pairs(self.input_dir_slash, ignored_regex_objects)

        expected = {'a.txt': 'ac.txt',
                    'b.txt': 'bc.txt'
                    }

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
