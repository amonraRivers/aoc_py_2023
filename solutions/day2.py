""" day 2 of advent of code 2023 """
from parser import read_lines

bag = {"blue": 14, "red": 12, "green": 13}


def get_games(line):
    """get the number of games from the line"""
    games = line.split(";")
    return games


def check_possible_game(game):
    """check if the game is possible"""
    s = game.strip().split(",")
    print(s)
    valid = True
    for x in s:
        y = x.strip().split(" ")
        [number, color] = [y[0], y[1]]
        if int(number) > bag[color]:
            valid = False
            break
    return valid


def solution1(lines):
    """solution for part 1 of day 2"""
    su = 0
    for count, line in enumerate(lines):
        [i, g] = line.split(":")
        games = get_games(g)
        valid = True
        for game in games:
            if check_possible_game(game) == False:
                valid = False
                break
        if valid:
            su += count + 1
    print(su)
    return su


def get_minimum_cubes(games):
    """get the minimum number of cubes"""
    cubes = []
    power = 1
    hm = {"blue": 0, "red": 0, "green": 0}
    for game in games:
        s = game.strip().split(",")
        for x in s:
            y = x.strip().split(" ")
            [number, color] = [y[0], y[1]]
            if int(number) > hm[color]:
                hm[color] = int(number)
    for key in hm:
        power *= hm[key]
    return power


def solution2(lines):
    su = 0
    for count, line in enumerate(lines):
        [i, g] = line.split(":")
        games = get_games(g)
        su += get_minimum_cubes(games)
    print(su)
    return su


def solutions():
    """print both solutions for day 2"""
    lines = read_lines("../2023/day2.txt")
    solution1(lines)
    solution2(lines)
