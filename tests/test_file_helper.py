#!/usr/bin/env python3

import unittest
from diffie import file_helper
from diffie import expression_helper


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        self.data_dir = '../data'

    def test_directories_in_dir_recursive_dont_ignore(self):

        ignored_dirname_patterns = []
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive(self.data_dir,
                                                          ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {self.data_dir,
                    self.data_dir + '/input',
                    self.data_dir + '/input/test',
                    self.data_dir + '/output'
                    }
        self.assertEqual(expected, set(actual))

    def test_directories_in_dir_recursive_ignore_test(self):

        ignored_dirname_patterns = ['test']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_dirname_patterns)

        actual = file_helper.directories_in_dir_recursive(self.data_dir,
                                                          ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {self.data_dir,
                    self.data_dir + '/input',
                    self.data_dir + '/output'
                    }
        self.assertEqual(expected, set(actual))

    def test_files_in_dir(self):

        ignored_filename_patterns = ['\A\.$', '\A\.\.$', '\A\.DS_Store$']
        ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

        actual = file_helper.files_in_dir(self.data_dir + '/input/test',
                                          ignored_regex_objects)

        # Don't care about element order, so compare results using set instead of list
        expected = {'a.txt',
                    'ac.txt',
                    'b.txt',
                    'bc.txt',
                    'c.txt',
                    }

        self.assertEqual(expected, set(actual))

if __name__ == "__main__":
    unittest.main()
