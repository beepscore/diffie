#!/usr/bin/env python3

import unittest
import os

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from diffie import file_writer


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        pass

    def test_filename_from_url_root(self):
        actual = file_writer.filename_from_url("http://www.beepscore.com")
        expected = "httpwww.beepscore.com"
        self.assertEqual(expected, actual)

    def test_filename_from_url(self):
        actual = file_writer.filename_from_url("http://beepscore.com/hubcape/")
        expected = "httpbeepscore.comhubcape"
        self.assertEqual(expected, actual)

    # This test is not ideal because it depends upon developer machine
    def test_absolute_dir_path(self):
        test_dirname = "../websearcher_junk_ok_to_delete"
        actual = file_writer.absolute_dir_path(test_dirname)
        self.assertEqual('/Users/stevebaker/Documents/projects/pythonProjects/websearcher_junk_ok_to_delete',
                         actual, '')

    # This test is not ideal because it depends upon developer machine
    def test_absolute_file_path(self):
        test_dirname = "../websearcher_junk_ok_to_delete"
        test_filename = "junk.txt"
        actual = file_writer.absolute_file_path(test_dirname, test_filename)
        self.assertEqual('/Users/stevebaker/Documents/projects/pythonProjects/websearcher_junk_ok_to_delete/junk.txt',
                         actual, '')

    def test_create_directory(self):
        test_dirname = "../websearcher_junk_ok_to_delete"
        file_writer.create_directory(test_dirname)
        self.assertTrue(os.path.isdir(test_dirname), '')

    def test_create_file(self):
        test_dirname = "../junk"
        test_filename = "junk.txt"
        test_content = "junk_text"

        file_writer.create_file(test_dirname, test_filename, test_content)

        actual = file_writer.absolute_file_path(test_dirname, test_filename)
        self.assertTrue(os.path.isfile(actual), '')

if __name__ == "__main__":
    unittest.main()
