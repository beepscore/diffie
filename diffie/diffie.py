#!/usr/bin/env python3

import difflib

def string_from_file(filename):
    with open(filename) as a_file:
        string = a_file.read()
    return string

def difflib_ndiff(filename_a, filename_b):
    """
    returns differences between two files using difflib_ndiff
    https://docs.python.org/3/library/difflib.html
    """

    lines_a = []
    lines_b = []

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

    sequenceMatcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequenceMatcher.get_opcodes():
        if tag != 'equal':
            # opcode is not 'equal', e.g. it is something like 'replace', 'delete', 'insert'
            opcode = '{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2])
            results.append(opcode)

    return results

def start_indexes_a(filename_a, filename_b):
    """
    returns indices from string_a opcode
    """
    with open(filename_a) as file_a:
        a = file_a.read()

    with open(filename_b) as file_b:
        b = file_b.read()

    results = []

    sequenceMatcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequenceMatcher.get_opcodes():
        if tag != 'equal':
            results.append(i1)
    return results

def start_indexes_b(filename_a, filename_b):
    """
    returns indices from string_b opcode
    """
    with open(filename_a) as file_a:
        a = file_a.read()

    with open(filename_b) as file_b:
        b = file_b.read()

    results = []

    sequenceMatcher = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sequenceMatcher.get_opcodes():
        if tag != 'equal':
            results.append(j1)
    return results

def start_index(index):
    if (index - 15) < 0:
        return 0
    else:
        return index

def pieces_string_a(filename_a, filename_b):
    """
    return pieces of text from filename_a
    """
    string_a = string_from_file(filename_a)
    start_indexes = start_indexes_a(filename_a, filename_b)
    pieces_a = []

    for index in start_indexes:
#        start = start_index(index)
#        end = end_index(index, string_a)
        pieces_a.append(string_a[index-15:index+15])

    return pieces_a
