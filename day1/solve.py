with open('input.txt','r') as f:
    measurements = [int(x) for x in f.readlines()]

#1st part
counter = 0
for i in range(1, len(measurements)):
    if measurements[i] > measurements[i - 1]:
        counter += 1
print(counter)

#2nd part
counter = 0
for i in range(3, len(measurements)):
    if measurements[i - 2] + measurements[i - 1] + measurements[i] > measurements[i - 3] + measurements[i - 2] + measurements[i - 1]:
        counter += 1
print(counter)