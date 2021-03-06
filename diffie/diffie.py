#!/usr/bin/env python3

import difflib
import os

from diffie import expression_helper
from diffie import file_pairer
from diffie import file_writer


def string_from_file(filename):
    with open(filename) as a_file:
        string = a_file.read()
    return string


def difflib_ndiff(filename_a, filename_b):
    """
    returns differences between two files using difflib_ndiff
    https://docs.python.org/3/library/difflib.html
    """

    with open(filename_a) as file_a:
        lines_a = file_a.readlines()

    with open(filename_b) as file_b:
        lines_b = file_b.readlines()

    results = list(difflib.ndiff(lines_a, lines_b))
    return results


def sequence_matcher_opcodes_no_equal(filename_a, filename_b):
    """
    returns differences between two files using get_opcodes
    filters out opcodes whose tag is 'equal'
    https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_grouped_opcodes
    """

    with open(filename_a) as file_a:
        a = file_a.read()

    with open(filename_b) as file_b:
        b = file_b.read()

    results = []

    sequence_matcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequence_matcher.get_opcodes():
        if tag != 'equal':
            # opcode is not 'equal', e.g. it is something like 'replace', 'delete', 'insert'
            opcode = '{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2])
            results.append(opcode)

    return results


def opcode_indexes_a(filename_a, filename_b):
    """
    returns start and end indexes from string_a opcode
    """
    with open(filename_a) as file_a:
        a = file_a.read()

    with open(filename_b) as file_b:
        b = file_b.read()

    results = []

    sequence_matcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequence_matcher.get_opcodes():
        if tag != 'equal':
            results.append((i1, i2))
    return results


def opcode_indexes_b(filename_a, filename_b):
    """
    returns start and end indexes from string_b opcode
    """
    with open(filename_a) as file_a:
        a = file_a.read()

    with open(filename_b) as file_b:
        b = file_b.read()

    results = []

    sequence_matcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequence_matcher.get_opcodes():
        if tag != 'equal':
            results.append((j1, j2))
    return results


def start_index(opcode_start_index):
    number_of_characters_before = 20
    proposed_start = opcode_start_index - number_of_characters_before
    if proposed_start < 0:
        return 0
    else:
        return proposed_start


def end_index(opcode_start_index, string):
    number_of_characters_after = 20
    proposed_end = opcode_start_index + number_of_characters_after
    if proposed_end > len(string) - 1:
        return len(string) - 1
    else:
        return proposed_end


def pieces_string_a(filename_a, filename_b):
    """
    return pieces of text from filename_a
    """
    string_a = string_from_file(filename_a)
    indexes = opcode_indexes_a(filename_a, filename_b)
    pieces_a = []

    for opcode_indexes in indexes:
        start = start_index(opcode_indexes[0])
        end = end_index(opcode_indexes[1], string_a)
        pieces_a.append(string_a[start:end])

    return pieces_a


def pieces_string_b(filename_a, filename_b):
    """
    return pieces of text from filename_b
    """
    string_b = string_from_file(filename_b)
    indexes = opcode_indexes_b(filename_a, filename_b)
    pieces_b = []

    for opcode_indexes in indexes:
        start = start_index(opcode_indexes[0])
        end = end_index(opcode_indexes[1], string_b)
        pieces_b.append(string_b[start:end])

    return pieces_b


def pieces(filename_a, filename_b):
    """
    return differing pieces of text from filename_a and filename_b
    """
    pieces_a = pieces_string_a(filename_a, filename_b)
    pieces_b = pieces_string_b(filename_a, filename_b)
    pieces_a_b = []

    for index, piece_a in enumerate(pieces_a):
        pieces_a_b.append((piece_a, pieces_b[index]))

    return pieces_a_b


def pieces_lines(filename_a, filename_b):
    """
    return differing pieces of text from filename_a and filename_b
    """
    pieces_a = pieces_string_a(filename_a, filename_b)
    pieces_b = pieces_string_b(filename_a, filename_b)
    pieces_a_b = ""

    for index, piece_a in enumerate(pieces_a):
        pieces_a_b += piece_a + os.linesep
        pieces_a_b += pieces_b[index] + os.linesep
        pieces_a_b += os.linesep

    return pieces_a_b


def get_pieces_and_write(filename_a, filename_b, in_dir, out_dir, out_file):

    if (in_dir is not None) and (in_dir is not ""):
        filename_a = os.path.join(in_dir, filename_a)
        filename_b = os.path.join(in_dir, filename_b)

    pieces_a_b = pieces(filename_a, filename_b)
    # convert list to string
    pieces_a_b_string = "({})".format(pieces_a_b)

    file_writer.create_file(out_dir, out_file, pieces_a_b_string)


def get_pieces_lines_and_write(filename_a, filename_b, in_dir, out_dir, out_file):

    if (in_dir is not None) and (in_dir != ""):
        filename_a = os.path.join(in_dir, filename_a)
        filename_b = os.path.join(in_dir, filename_b)

    pieces_a_b_string = pieces_lines(filename_a, filename_b)

    file_writer.create_file(out_dir, out_file, pieces_a_b_string)


def get_diffs_write(in_dir, out_dir, out_file):

    ignored_filename_patterns = ['\a\.$', '\a\.\.$', '\a\.ds_store$']
    ignored_regex_objects = expression_helper.regex_objects_from_patterns(ignored_filename_patterns)

    file_pairs = file_pairer.file_pairs("./data/input", ignored_regex_objects)

    file_writer.create_file(out_dir, out_file, None)
    out_file = os.path.join(out_dir, out_file)
    print("out_file {}".format(out_file))

    # dictionary is not sorted, and order can vary. Sort keys to iterate files in alphabetical order.
    keys_sorted = sorted(file_pairs.keys())

    for key in keys_sorted:
        # print("key {}, value {}".format(key, file_pairs[key]))

        filename_a = key
        filename_b = file_pairs[key]

        if (in_dir is not None) and (in_dir != ""):
            filename_a = os.path.join(in_dir, filename_a)
            filename_b = os.path.join(in_dir, filename_b)

        pieces_a_b_string = pieces_lines(filename_a, filename_b)
        # print("pieces_a_b_string {}".format(pieces_a_b_string))

        with open(out_file, "a") as myfile:
            myfile.write("files {} {}\n".format(filename_a, filename_b))
            myfile.write(pieces_a_b_string)
            myfile.write("\n")

    myfile.close()
