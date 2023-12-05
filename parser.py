"""This module contains the functions for parsing the input file"""


def read_lines(path):
    """read the lines of the specified file"""
    with open(path, "r", encoding="utf-8") as file1:
        lines = file1.readlines()
        return lines
