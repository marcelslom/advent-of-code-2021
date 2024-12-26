def find_low_points_in_marginal_row(row_number, adjacent_row_number):
    lp = []
    row = HEATMAP[row_number]
    adjacent_row = HEATMAP[adjacent_row_number]
    for x in range(1, len(row) - 1):
        if (row[x] < row[x-1]
        and row[x] < row[x+1]
        and row[x] < adjacent_row[x]):
            lp.append([row_number, x])
    return lp

def find_low_points_in_marginal_column(column_number, adjacent_column_number):
    lp = []
    column, adjacent_column = [row[column_number] for row in HEATMAP], [row[adjacent_column_number] for row in HEATMAP]
    for y in range(1, len(column) - 1):
        if (column[y] < column[y-1]
        and column[y] < column[y+1]
        and column[y] < adjacent_column[y]):
            lp.append([y, column_number])
    return lp

def corner_is_low_point(value, adjacent_first, adjacent_second):
    return value < adjacent_first and value < adjacent_second

def find_low_points():
    low_points = []
    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            if (HEATMAP[y][x] < HEATMAP[y-1][x]
            and HEATMAP[y][x] < HEATMAP[y+1][x]
            and HEATMAP[y][x] < HEATMAP[y][x-1]
            and HEATMAP[y][x] < HEATMAP[y][x+1]):
                low_points.append([y, x])

    low_points += find_low_points_in_marginal_row(0, 1)
    low_points += find_low_points_in_marginal_row(HEIGHT - 1, HEIGHT - 2)
    low_points += find_low_points_in_marginal_column(0, 1)
    low_points += find_low_points_in_marginal_column(WIDTH - 1, WIDTH - 2)

    if corner_is_low_point(HEATMAP[0][0], HEATMAP[0][1], HEATMAP[1][0]):
        low_points.append([0, 0])
    if corner_is_low_point(HEATMAP[0][WIDTH - 1], HEATMAP[0][WIDTH - 2], HEATMAP[1][WIDTH - 1]):
        low_points.append([0, WIDTH - 1])
    if corner_is_low_point(HEATMAP[HEIGHT - 1][0], HEATMAP[HEIGHT - 1][1], HEATMAP[HEIGHT - 2][0]):
        low_points.append([HEIGHT - 1, 0])
    if corner_is_low_point(HEATMAP[HEIGHT - 1][WIDTH - 1], HEATMAP[HEIGHT - 1][WIDTH - 2], HEATMAP[HEIGHT - 2][WIDTH - 1]):
        low_points.append([HEIGHT - 1, WIDTH - 1])
    
    return low_points

HEATMAP = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        HEATMAP.append([int(x) for x in list(line.strip())])

HEIGHT = len(HEATMAP)
WIDTH = len(HEATMAP[0])

low_points = find_low_points()

#1st part
def calc_risk(low_point):
    return HEATMAP[low_point[0]][low_point[1]] + 1

risks = sum([calc_risk(low_point) for low_point in low_points])
print(risks)

#2nd part
def get_neighbours(point):
    neighbours = []
    y, x = point
    if y > 0:
        neighbours.append([y - 1, x])
    if y < HEIGHT - 1:
        neighbours.append([y + 1, x])
    if x > 0:
        neighbours.append([y, x - 1])
    if x < WIDTH - 1:
        neighbours.append([y, x + 1])
    return neighbours

def visit(basin_map, point):
    y, x = point
    basin_map[y][x] = True
    neighbours = get_neighbours(point)
    for n in neighbours:
        ny, nx = n
        if not basin_map[ny][nx] and HEATMAP[ny][nx] is not 9:
                visit(basin_map, n)

def calculate_basin_size(low_point):
    basin_map = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
    visit(basin_map, low_point)
    return sum([row.count(True) for row in basin_map])

sizes = []    
for point in low_points:
    sizes.append(calculate_basin_size(point))

sizes = sorted(sizes)[-3:]
result = sizes[0] * sizes[1] * sizes[2]
print(result)


