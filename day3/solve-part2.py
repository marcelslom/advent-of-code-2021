def oxygen_criteria(number_of_ones, number_of_lines):
    return '1' if number_of_ones >= number_of_lines / 2 else '0'

def co2_criteria(number_of_ones, number_of_lines):
    return '1' if oxygen_criteria(number_of_ones, number_of_lines) == '0' else '0'

def calculate(lines, position):
    number_of_ones = 0
    for line in lines:
        if line[position] == '1':
            number_of_ones += 1
    return number_of_ones

def find(lines, criteria):
    line_len = len(lines[0])
    to_filter = lines
    for i in range(line_len):
        number_of_ones = calculate(to_filter, i)
        crit = criteria(number_of_ones, len(to_filter))
        filtered = list(filter(lambda x: x[i] == crit, to_filter))
        if len(filtered) == 1:
            return filtered[0]
        else:
            to_filter = filtered

with open('input-3.txt', 'r') as f:
    lines = f.readlines()

oxygen = int(find(lines, oxygen_criteria), 2)
co2 = int(find(lines, co2_criteria), 2)

print(oxygen)
print(co2)
print(oxygen * co2)
