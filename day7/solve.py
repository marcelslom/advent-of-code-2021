def calculate_fuel_1(crabs, position):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - position)
    return fuel

def calculate_fuel_2(crabs, position):
    fuel = 0
    for crab in crabs:
        fuel += sigma(abs(crab - position))
    return fuel

def sigma(n):
    if n % 2 is 1:
        return n * int((n // 2 + 1))
    else:
        return (n - 1) * int((n / 2)) + n


def solve(crabs, calculate_function):
    min_position = 0
    min_fuel = calculate_function(crabs, min_position)
    for i in range(1, max(crabs)):
        d = calculate_function(crabs, i)
        if d < min_fuel:
            min_fuel = d
            min_position = i

    print(min_position)
    print(min_fuel)


with open('input.txt','r') as f:
    crabs = [int(x) for x in f.readline().strip().split(',')]

#1st part
solve(crabs, calculate_fuel_1)

#2nd part
solve(crabs, calculate_fuel_2)

