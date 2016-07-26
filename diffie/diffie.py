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

def opcode_start_indexes_a(filename_a, filename_b):
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

def opcode_start_indexes_b(filename_a, filename_b):
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

def start_index(opcode_start_index):
    number_of_characters_before = 15
    proposed_start = opcode_start_index - number_of_characters_before
    if proposed_start < 0:
        return 0
    else:
        return proposed_start

def end_index(opcode_start_index, string):
    number_of_characters_after = 15
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
    start_indexes = opcode_start_indexes_a(filename_a, filename_b)
    pieces_a = []

    for opcode_start_index in start_indexes:
        start = start_index(opcode_start_index)
        end = end_index(opcode_start_index, string_a)
        # print(opcode_start_index, opcode_start_index - 15, opcode_start_index + 15, 'start: ', start, 'end:', end)
        pieces_a.append(string_a[start:end])

    return pieces_a

def pieces_string_b(filename_a, filename_b):
    """
    return pieces of text from filename_b
    """
    string_b = string_from_file(filename_b)
    start_indexes = opcode_start_indexes_b(filename_a, filename_b)
    pieces_b = []

    for opcode_start_index in start_indexes:
        start = start_index(opcode_start_index)
        end = end_index(opcode_start_index, string_b)
        pieces_b.append(string_b[start:end])

    return pieces_b

def pieces(filename_a, filename_b):
    """
    return differing pieces of text from filename_a and filename_b
    """
    string_a = string_from_file(filename_a)
    string_b = string_from_file(filename_b)
    start_indexes_a = opcode_start_indexes_a(filename_a, filename_b)
    pieces_a = []
    pieces_b = []
    pieces_a_b = []

    for index in start_indexes_a:
        start = start_index(index)
        end_a = end_index(index, string_a)
        end_b = end_index(index, string_b)
        # print(index, index - 15, index + 15, 'start: ', start, 'end:', end)
        pieces_a_b.append(string_a[start:end_a])
        pieces_a_b.append(string_b[start:end_b])
        # add separator to make it easier to visually scan pairs
        pieces_a_b.append('')

    return pieces_a_b

