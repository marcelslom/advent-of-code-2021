class Incomplete(Exception):

    def __init__(self, completion_string) -> None:
        super().__init__(None)
        self.missing_string = completion_string


class Corrupted(Exception):
    
    def __init__(self, expected, found) -> None:
        super().__init__(None)
        self.expected = expected
        self.found = found


BRACKETS = dict()
BRACKETS['('] = ')'
BRACKETS['['] = ']'
BRACKETS['{'] = '}'
BRACKETS['<'] = '>'

def parse(line):
    stack = []
    for c in line:
        if c in BRACKETS.keys():
            stack.append(c)
        elif c in BRACKETS.values():
            opening = stack.pop()
            expected = BRACKETS[opening]
            if c != expected:
                raise Corrupted(expected, c)
        else:
            raise Exception(f'Unexpected char {c}')
            
    if stack:
        completion_string = ''
        while stack:
            opening = stack.pop()
            completion_string += BRACKETS[opening]
        
        raise Incomplete(completion_string)


with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

#1st part
illegal_points = dict()
illegal_points[')'] = 3
illegal_points[']'] = 57
illegal_points['}'] = 1197
illegal_points['>'] = 25137

total = 0
for line in lines:
    try:
        parse(line)
    except Incomplete:
        pass
    except Corrupted as e:
        total += illegal_points[e.found]

print(total)

#2nd part
missing_points = dict()
missing_points[')'] = 1
missing_points[']'] = 2
missing_points['}'] = 3
missing_points['>'] = 4

missing_scores = []
for line in lines:
    try:
        parse(line)
    except Incomplete as e:
        points = 0
        for c in e.missing_string:
            points *= 5
            points += missing_points[c]
        missing_scores.append(points)
    except Corrupted:
        pass

missing_scores = sorted(missing_scores)
print(missing_scores[len(missing_scores)//2])