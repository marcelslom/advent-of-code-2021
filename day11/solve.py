class Octopus:

    def __init__(self, energy, y, x, on_flash_callback) -> None:
        self.energy = energy
        self.y = y
        self.x = x
        self.on_flash_callback = on_flash_callback
        self.flashed = False

    def inc_energy(self):
        self.energy += 1

    def flash(self):
        if not self.flashed and self.energy > 9:
            self.flashed = True
            self.on_flash_callback(self.y, self.x)

    def reset(self):
        if self.flashed:
            self.energy = 0
            self.flashed = False


def get_adjacent_octopuses(octopuses, y, x):
    adjacent = []

    if y > 0:
        adjacent.append(octopuses[y - 1][x])
        if x > 0:
            adjacent.append(octopuses[y - 1][x - 1])
        if x < len(octopuses[y]) - 1:
            adjacent.append(octopuses[y - 1][x + 1])
    if y < len(octopuses) - 1:
        adjacent.append(octopuses[y + 1][x])
        if x > 0:
            adjacent.append(octopuses[y + 1][x - 1])
        if x < len(octopuses[y]) - 1:
            adjacent.append(octopuses[y + 1][x + 1])
    if x > 0:
        adjacent.append(octopuses[y][x - 1])
    if x < len(octopuses[y]) - 1:
        adjacent.append(octopuses[y][x + 1])
    
    return adjacent

def on_flash(y, x):
    adjacent = get_adjacent_octopuses(OCTOPUSES, y, x)
    for octopus in adjacent:
        octopus.inc_energy()
        octopus.flash()

def step():
    for row in OCTOPUSES:
        for octopus in row:
            octopus.inc_energy()

    for row in OCTOPUSES:
        for octopus in row:
            octopus.flash()

    number_of_flashes = 0
    for row in OCTOPUSES:
        number_of_flashes += sum(oct.flashed for oct in row)

    for row in OCTOPUSES:
        for octopus in row:
            octopus.reset()

    return number_of_flashes

def load_octopuses():
    octopuses = []
    with open('input.txt', 'r') as f:
        for y, line in enumerate(f.readlines()):
            row = []
            for x, energy in enumerate(line.strip()):
                row.append(Octopus(int(energy), y, x, on_flash))
            octopuses.append(row)
    return octopuses

#1st step
OCTOPUSES = load_octopuses()

number_of_flashes = 0

for i in range(100):
    number_of_flashes += step()

print(number_of_flashes)

#2nd step
OCTOPUSES = load_octopuses()
number_of_octopuses = sum(len(y) for y in OCTOPUSES)

i = 1
number_of_flashes = step()

while number_of_flashes != number_of_octopuses:
    number_of_flashes = step()
    i += 1

print(i)