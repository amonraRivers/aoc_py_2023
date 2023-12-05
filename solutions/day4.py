"""advent of code day 3"""
from parser import read_lines


def get_number_lists(line):
    """get the number lists from the line"""
    lists = line.split(":")[1]
    lists = lists.strip().split("|")
    list1 = lists[0].strip().split()
    list2 = lists[1].strip().split()
    return (list1, list2)


def get_winning_numbers(ls):
    lst3 = list(set(ls[0]) & set(ls[1]))
    return lst3


def solution1(lists):
    """solution for part 1 of day 3"""
    s = 0
    for line in lists:
        lst3 = get_winning_numbers(line)
        if len(lst3) == 0:
            t = 0
        else:
            t = 2 ** max(len(lst3) - 1, 0)
        s += t
    print(s)


def solution2(lists):
    """solution for part 2 of day 3"""
    s = 0
    to_process = [1] * len(lists)
    index = 0
    while index < len(lists):
        i = to_process[index]
        s += i
        lst3 = get_winning_numbers(lists[index])
        for x in range(len(lst3)):
            to_process[index + x + 1] += i
        index += 1
    print(s)


def solutions():
    """return solutions for day 3"""
    lines = read_lines("../2023/day4.txt")
    lists = [get_number_lists(line) for line in lines]
    solution1(lists)
    solution2(lists)
