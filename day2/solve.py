commands = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        cmd, val = line.split()
        val = int(val)
        commands.append([cmd, val])

#1st part
forward = 0
up = 0
down = 0

for cmd, val in commands:
    if cmd == 'forward':
        forward += val
    elif cmd == 'up':
        up += val
    elif cmd =='down':
        down += val

print(forward * (down - up))

#2nd part
horizontal = 0
vertical = 0
aim = 0

for cmd, val in commands:
    if cmd == 'forward':
        horizontal += val
        vertical += aim * val
    elif cmd == 'up':
        aim -= val
    elif cmd =='down':
        aim += val

print(horizontal * vertical)