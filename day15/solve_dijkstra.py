import sys


class Node:

    def __init__(self, x: int, y: int, cost: int) -> None:
        self.x = x
        self.y = y
        self.cost = cost
        self.previous = None
        self.distance = sys.maxsize
        self.visited = False


class Dijkstra2D:

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

    def all_nodes_visited(self):
        for row in self.grid:
            if any(not node.visited for node in row):
                return False
        return True

    def visit(self, node):
        neighbours = self.get_neighbours(node)
        for neighbour in neighbours:
            if node.distance + neighbour.cost < neighbour.distance:
                neighbour.distance = node.distance + neighbour.cost
                neighbour.previous = node
        node.visited = True

    def get_node_with_minimal_distance(self):
        distance = sys.maxsize
        selected = None
        for row in self.grid:
            for node in row:
                if (not node.visited) and node.distance < distance:
                    selected = node
                    distance = node.distance
        return selected

    def solve(self):
        self.start_node.distance = 0
        while not self.all_nodes_visited():
            n = self.get_node_with_minimal_distance()
            self.visit(n)
        return self.finish_node.distance


GRID = []

with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, cost in enumerate(line.strip()):
            row.append(Node(x, y, int(cost)))
        GRID.append(row)

#1st part
def solve_1():
    solution = Dijkstra2D(GRID, 0, 0, -1, -1)
    dist = solution.solve()
    print(f'1st part solution is {dist}')

solve_1()