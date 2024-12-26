class Line:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

        self.subpoints = []
        if self.is_horizontal():
            x_start = min(self.start[0], self.end[0])
            x_end = max(self.start[0], self.end[0])
            for i in range(x_start, x_end + 1):
                self.subpoints.append(tuple([i, start[1]]))
        elif self.is_vertical():
            y_start = min(self.start[1], self.end[1])
            y_end = max(self.start[1], self.end[1])
            for i in range(y_start, y_end + 1):
                self.subpoints.append(tuple([start[0], i]))
        else:
            gradient_x = 1 if self.end[0] > self.start[0] else -1
            gradient_y = 1 if self.end[1] > self.start[1] else -1
            number_of_points = abs(end[0] - start[0]) + 1
            for i in range(number_of_points):
                s_x = start[0] + i * gradient_x
                s_y = start[1] + i * gradient_y
                self.subpoints.append(tuple([s_x, s_y]))

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

def solve(lines):
    occurences = dict()

    for line in lines:
        for point in line.subpoints:
            occurences[point] = occurences.get(point, 0) + 1

    print(len([k for k,v in occurences.items() if v >= 2]))

lines = []

with open('input.txt', 'r') as f:
    for file_line in f.readlines():
        coords = file_line.split(' -> ')
        start = tuple([int(x) for x in coords[0].split(',')])
        end = tuple([int(x) for x in coords[1].split(',')])
        lines.append(Line(start,end))

#1st part
solve([line for line in lines if line.is_horizontal() or line.is_vertical()])

#2nd part
solve(lines)
