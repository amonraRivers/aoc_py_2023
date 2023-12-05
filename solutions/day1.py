"""
Day 1 solutions.
"""
from parser import read_lines


def change_line_to_numbers(line):
    """change text numbers to actual ints"""
    dict = {
        "zero": "z0o",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    l = line[:]
    for key in dict:
        l = l.replace(key, str(dict[key]))
    return l


def solution1(lines):
    """solution for part 1 of day 1"""
    sum = 0
    for line in lines:
        first = 0
        last = 0
        for x in line:
            if x.isdigit():
                first = int(x) * 10
                break
        for x in line[::-1]:
            if x.isdigit():
                last = int(x)
                break
        sum += first + last

    print(sum)


def solution2(lines):
    """solution for part 2 of day 1"""
    sum = 0
    for line in lines:
        first = 0
        last = 0
        l = change_line_to_numbers(line)
        for x in l:
            if x.isdigit():
                first = int(x) * 10
                break
        for x in l[::-1]:
            if x.isdigit():
                last = int(x)
                break
        sum += first + last

    print(sum)


def solutions():
    """print both solutions for day 1"""
    lines = read_lines("../2023/day1.txt")
    solution1(lines)
    solution2(lines)
