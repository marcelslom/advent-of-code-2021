CAVES = {}

with open('input.txt','r') as f:
    for line in f.readlines():
        x, y = line.strip().split('-')
        try:
            CAVES[x].add(y)
        except KeyError:
            CAVES[x] = {y}

        try:
            CAVES[y].add(x)
        except KeyError:
            CAVES[y] = {x}

#1st part
def visit(cave, small_caves_visited):
    if cave == 'end':
        return 1

    if cave.islower():
        small_caves_visited.add(cave)
    
    visited_paths = 0
    for cave_to_visit in CAVES[cave]:
        if not cave_to_visit in small_caves_visited:
            visited_paths += visit(cave_to_visit, small_caves_visited.copy())

    return visited_paths

number_of_visited = visit('start', set())
print(number_of_visited)


#2nd part
def second_part():

    paths = set()

    def visit(cave, visited_small_caves, special_cave, number_of_visits_in_special_cave, path):
        path = path + ',' + cave

        if cave == 'end':
            paths.add(path)
            return

        if cave == special_cave:
            if number_of_visits_in_special_cave < 2:
                number_of_visits_in_special_cave += 1
            else:
                return
        elif cave.islower():
            visited_small_caves.add(cave)

        for cave_to_visit in CAVES[cave]:
            if not cave_to_visit in visited_small_caves:
                visited = visited_small_caves.copy()
                visit(cave_to_visit, visited, special_cave, number_of_visits_in_special_cave, path)


    small = [x for x in CAVES.keys() if x.islower() and x != 'start' and x != 'end']
    for s in small:
        visit('start', set(), s, 0, '')
    print(len(paths))

second_part()