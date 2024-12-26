import collections

with open('input.txt', 'r') as f:
    lines = f.readlines()
    TEMPLATE = lines[0].strip()
    RULES = dict()

    for i in range(2, len(lines)):
        k, v = lines[i].strip().split(' -> ')
        RULES[k] = v


#1st part
def step(input_polymer):
    to_insert = []
    for i in range(len(input_polymer) - 1):
        pair = input_polymer[i:i+2]
        if pair in RULES.keys():
            to_insert.append(RULES[pair])
        else:
            to_insert.append('')

    result = ''
    for i in range(len(input_polymer)):
        result += input_polymer[i]
        if i < len(input_polymer) - 1:
            result += to_insert[i]
    
    return result

polymer = TEMPLATE
for i in range(10):
    polymer = step(polymer)

sorted = collections.Counter(polymer).most_common()
print(sorted[0][1] - sorted[-1][1])


#2nd part
def transform_polymer(polymer_pairs):
    transformed = collections.defaultdict(int)
    for key, value in polymer_pairs.items():
        if key in RULES:
            pair_1 = key[0] + RULES[key]
            pair_2 = RULES[key] + key[1]
            transformed[pair_1] += value
            transformed[pair_2] += value
        else:
            transformed[key] = value
    return transformed

def convert_polymer_to_pairs(polymer):
    polymer_dict = collections.defaultdict(int)
    for i in range(len(polymer) - 1):
        pair = polymer[i: i + 2]
        polymer_dict[pair] += 1
    return polymer_dict

def count_letters(polymer):
    counter = collections.defaultdict(int)
    for key, value in polymer.items():
        counter[key[0]] += value
        counter[key[1]] += value
    return counter


polymer_pairs = convert_polymer_to_pairs(TEMPLATE)

for i in range(40):
    polymer_pairs = transform_polymer(polymer_pairs)

counted = count_letters(polymer_pairs)
counted[TEMPLATE[0]] += 1
counted[TEMPLATE[-1]] += 1

for k, v in counted.items():
    counted[k] = int(v / 2)

print(max(counted.values()) - min(counted.values()))