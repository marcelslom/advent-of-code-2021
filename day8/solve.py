DISPLAY_WIRING = dict()
DISPLAY_WIRING[0] = 'abcefg'
DISPLAY_WIRING[1] = 'cf'
DISPLAY_WIRING[2] = 'acdeg'
DISPLAY_WIRING[3] = 'acdfg'
DISPLAY_WIRING[4] = 'bcdf'
DISPLAY_WIRING[5] = 'abdfg'
DISPLAY_WIRING[6] = 'abdefg'
DISPLAY_WIRING[7] = 'acf'
DISPLAY_WIRING[8] = 'abcdefg'
DISPLAY_WIRING[9] = 'abcdfg'

entries = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input, output = line.split(' | ')
        input = [x.strip() for x in input.split(' ')]
        output = [x.strip() for x in output.split(' ')]
        entries.append([input, output])

#1st part
counter = 0
for entry in entries :
    for output in entry[1]:
        l = len(output)
        if (l is 2 or l is 3 or l is 4 or l is 7):
            counter += 1

print(counter)

#2nd part
def check_present_absent(input, length, element_to_compare):
    for x in input:
        if len(x) == length:
            if element_to_compare[0] in x and element_to_compare[1] not in x:
                return element_to_compare[0], element_to_compare[1], x
            if element_to_compare[1] in x and element_to_compare[0] not in x:
                return element_to_compare[1], element_to_compare[0], x

def find_wiring_mapping(input):
    input_to_process = input.copy()
    mapping = dict()

    one = [x for x in input_to_process if len(x) is 2][0]
    four = [x for x in input_to_process if len(x) is 4][0]
    seven = [x for x in input_to_process if len(x) is 3][0]
    eigth = [x for x in input_to_process if len(x) is 7][0]

    input_to_process.remove(one)
    input_to_process.remove(four)
    input_to_process.remove(seven)
    input_to_process.remove(eigth)

    a = list(set(seven) - set(one))[0]
    mapping[a] = 'a'
    f, c, six = check_present_absent(input_to_process, 6, one)
    mapping[f] = 'f'
    mapping[c] = 'c'
    input_to_process.remove(six)
    b_and_d = list(set(four) - set(one))
    b, d, zero = check_present_absent(input_to_process, 6, b_and_d)
    mapping[b] = 'b'
    mapping[d] = 'd'
    input_to_process.remove(zero)
    nine = [x for x in input_to_process if len(x) is 6][0]
    e = list(set(eigth) - set(nine))[0]
    mapping[e] = 'e'
    input_to_process.remove(nine)
    chars = 'abcdefg'
    for k in mapping.keys():
        chars = chars.replace(k, '')
    mapping[chars] = 'g'

    return mapping

def decode_digit(output, mapping):
    real_segments = ''
    for c in output:
        real_segments += mapping[c]
    real_segments = ''.join(sorted(real_segments))
    return [k for k, v in DISPLAY_WIRING.items() if v == real_segments][0]

sum = 0
for entry in entries:
    mapping = find_wiring_mapping(entry[0])
    result = 0
    outputs = entry[1]
    for i, output in enumerate(outputs):
        power = len(outputs) - i - 1
        digit = decode_digit(output, mapping)
        result += digit * (10 ** power)

    sum += result

print(sum)