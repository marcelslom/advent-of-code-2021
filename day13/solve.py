FOLD = []
DOTS = []

with open('input.txt','r') as f:
    for line in f.readlines():
        if line.startswith('fold along'):
            fold = line.replace('fold along ', '').split('=')
            FOLD.append([fold[0], int(fold[1].strip())])
        elif not line.strip():
            pass
        else:
            DOTS.append(tuple([int(x.strip()) for x in line.split(',')]))

def fold_paper(paper, instruction):
    axis, line = instruction
    folded = set()
    if axis == 'x':
        for dot in paper:
            if dot[0] < line:
                folded.add(dot)
            else:
                x = line - (dot[0] - line)
                folded.add(tuple([x, dot[1]]))
    else:
        for dot in paper:
            if dot[1] < line:
                folded.add(dot)
            else:
                y = line - (dot[1] - line)
                folded.add(tuple([dot[0], y]))
    return folded


#1st part
instruction = FOLD[0]
folded = fold_paper(DOTS, instruction)
print(len(folded))

#2nd part
folded = DOTS
for instruction in FOLD:
    folded = fold_paper(folded, instruction)

from operator import itemgetter

y = int(max(folded, key=itemgetter(1))[1])
x = int(max(folded, key=itemgetter(0))[0])

for i in range(y + 1):
    for j in range(x + 1):
        if tuple([j, i]) in folded:
            print('#', end = '')
        else:
            print('.', end = '')
    print()