d = dict()

with open('input-3.txt', 'r') as f:
    lines = f.readlines()
    nol = len(lines)
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                d[i] = d.get(i, 0) + 1

binary_gamma = ''.join(['1' if d[i] > nol/2 else '0' for i in range(len(d))])
binary_epsilon = ''.join(['1' if d[i] < nol/2 else '0' for i in range(len(d))])

gamma = int(binary_gamma, 2)
epsilon = int(binary_epsilon, 2)

print(gamma)
print(epsilon)
print(gamma * epsilon)