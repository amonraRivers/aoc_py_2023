"""advent of code day 5"""
import sys
from parser import read_lines


class Link:
    def __init__(self, base, diff, amount):
        self.diff = diff
        self.base = base
        self.amount = amount

    def inverse_link(self):
        return Link(self.base + self.diff, -self.diff, self.amount)

    def add_to_nodes(self, node1, node2):
        links1 = node1.get_links(node2)
        links2 = node2.get_links(node1)
        links1.append(self)
        links2.append(self.inverse_link())

    def __str__(self):
        return str(self.base) + " " + str(self.diff) + " " + str(self.amount)

    def __repr__(self):
        return str(self)


class Node:
    def __init__(self, name):
        self.links = {}
        self.name = name

    def get_links(self, node):
        if node.name not in self.links:
            self.links[node.name] = []
        return self.links[node.name]

    def find_next(self, node, value):
        links = self.get_links(node)
        for link in links:
            if link.base <= int(value) < link.base + link.amount:
                return int(value) + link.diff
        return value

    def __str__(self):
        return self.name + " " + str(self.links)

    def __repr__(self):
        return str(self)


def create_nodes(lines):
    get_header = False
    node1 = None
    node2 = None
    nodes = {}
    times = 0
    for line in lines:
        if line == "\n":
            get_header = True
            times = 1
            continue
        if times == 1:
            if get_header:
                ns = line.split(" ")[0].split("-")
                if nodes.get(ns[0]) is None:
                    nodes[ns[0]] = Node(ns[0])
                if nodes.get(ns[2]) is None:
                    nodes[ns[2]] = Node(ns[2])
                node1 = nodes[ns[0]]
                node2 = nodes[ns[2]]
                get_header = False
            else:
                values = line.split(" ")
                link = Link(
                    int(values[1]), int(values[0]) - int(values[1]), int(values[2])
                )
                link.add_to_nodes(node1, node2)
    return nodes


def create_links(lines):
    get_header = False
    links = []
    times = 0
    for line in lines:
        if line == "\n":
            get_header = True
            times = 1
            links.append([])
            continue
        if times == 1:
            if get_header:
                get_header = False
            else:
                values = line.split(" ")
                link = Link(
                    int(values[1]), int(values[0]) - int(values[1]), int(values[2])
                )
                links[-1].append(link)
    return links


def solution1(seeds, lines):
    """solution for part 1 of day 5"""
    nodes = create_nodes(lines[1:])
    locations = []
    for seed in seeds:
        aux = None
        res = seed
        for node in nodes.values():
            if aux is not None:
                res = aux.find_next(node, res)
            aux = node
        locations.append(res)
    print(locations)
    print(min(locations))

def merge_links(l0,l1):
    res=[]
    edges=[]
    diffs=[]
    amounts=[]
    if (
            l0.base + l0.diff < l1.base + l1.amount":"
        and l1.base < l0.base + l0.diff + l1.amount
    ):

        # first link
        if l0.base+l0.diff<l1.base:
            edges.append(l0.base)
            amounts.append(l1.base-l0.base-l0.diff)
            diffs.append(l0.diff)
        else:
            if(l0.base+l0.diff!=l1.base):
                edges.append(l0.base)
                amounts.append(l1.base-l0.base-l0.diff)
                diffs.append(l0.diff)
        #second link
        edges.append(max(l0.base,l1.base-l0.diff))
        amounts.append((min(l0.base+l0.amount-l1.base,l1.amount)))
        diffs.append(l0.diff+l1.diff)

        #third link
        if l0.base+l0.amount<l1.base+l1.amount:
            edges.append(l0.base)
            amounts.append(l1.base-l0.base-l0.diff)
            diffs.append(l0.diff)
        else:
            if(l0.base+l0.diff!=l1.base):
                edges.append(l0.base)
                amounts.append(l1.base-l0.base-l0.diff)
                diffs.append(l0.diff)






def merge_link_lists(links0,links1):
    res = []
    aux=links0[:]
    for link1 in links1:
        for link0 in res[:]:
                    
    return res


def solution2(seeds, lines):
    """solution for part 2 of day 3"""
    res = []
    links = create_links(lines[1:])


def solutions():
    """return solutions for day 3"""
    lines = read_lines("../../2023/day5.txt")
    seeds = lines[0].split(":")[1].strip().split()

    solution1(seeds, lines)
    solution2(seeds, lines)
