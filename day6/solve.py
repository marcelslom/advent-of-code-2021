def solve(fishes, days):
    fishes_days = [0] * 9
    for i in range(len(fishes_days)):
        fishes_days[i] = len([fish for fish in fishes if fish == i])

    for i in range(days):
        fishes_to_born = fishes_days[0]
        for i in range(1, 9):
            fishes_days[i-1] = fishes_days[i]
        fishes_days[8] = fishes_to_born
        fishes_days[6] += fishes_to_born

    print(sum(fishes_days))

with open ('input.txt', 'r') as f:
    fishes = tuple([int(x) for x in f.readline().strip().split(',')])

#1st part
solve(fishes, 80)

#2nd part
solve(fishes, 256)