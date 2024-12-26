import sys
from queue import PriorityQueue

class Node:

    def __init__(self, x: int, y: int, cost: int) -> None:
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = None
        self.f = sys.maxsize
        self.g = sys.maxsize
        self.h = sys.maxsize

    def update_f(self):
        self.f = self.g + self.h

    def __eq__(self, other) -> bool:
        return self.f == other.f

    def __lt__(self, other) -> bool:
        return self.f < other.f


class Astar:

    def __init__(self, grid, start_x, start_y, finish_x, finish_y) -> None:
        self.grid = grid
        self.start_node = grid[start_y][start_x]
        self.finish_node = grid[finish_y][finish_x]

    def get_neighbours(self, node):
        neighbours = []
        positions = [[node.x - 1, node.y], [node.x + 1, node.y], [node.x, node.y - 1], [node.x, node.y + 1]]
        for position in positions:
            x = position[0]
            y = position[1]
            if x < self.start_node.x or x > self.finish_node.x or y < self.start_node.y or y > self.finish_node.y:
                continue
            neighbours.append(self.grid[y][x])
        return neighbours

    def get_h(self, node, finish_node):
        return abs(node.x - finish_node.x) + abs(node.y - finish_node.y)

    def solve(self):
        open = PriorityQueue()
        start_node = self.start_node
        start_node.f = 0
        start_node.g = 0
        start_node.h = 0
        open.put(start_node)
        while not open.empty():
            node = open.get()
            if node is self.finish_node:
                return node
            neighbours = self.get_neighbours(node)
            for neighbour in neighbours:
                new_g = node.g + neighbour.cost
                if new_g < neighbour.g:
                    neighbour.g = new_g
                    neighbour.h = self.get_h(neighbour, self.finish_node)
                    neighbour.update_f()
                    neighbour.parent = node
                    open.put(neighbour)


GRID = []

with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, cost in enumerate(line.strip()):
            row.append(Node(x, y, int(cost)))
        GRID.append(row)


#2nd part
def generate_subgrid(base, offset_x, offset_y):
    new_grid = []
    for row in base:
        new_row = []
        for element in row:
            new_x = element.x + offset_x * len(row)
            new_y = element.y + offset_y * len(row)
            offset = offset_x + offset_y
            new_cost = element.cost + offset
            if new_cost > 9:
                new_cost = new_cost - 9
            new_row.append(Node(new_x, new_y, new_cost))
        new_grid.append(new_row)
    return new_grid

import numpy
subgrids = [[0 for x in range(5)] for y in range(5)] 
for y in range(5):
    for x in range(5):
        subgrids[y][x] =numpy.array(generate_subgrid(GRID, x, y))


EXTENDED_GRID = numpy.concatenate(subgrids[0], axis=1)

for i in range(1, 5):
    row = numpy.concatenate(subgrids[i], axis=1)
    EXTENDED_GRID = numpy.concatenate((EXTENDED_GRID, row), axis=0)

EXTENDED_GRID = EXTENDED_GRID.tolist()

astar = Astar(EXTENDED_GRID, 0, 0, -1, -1)
finish = astar.solve()
print(finish.g)