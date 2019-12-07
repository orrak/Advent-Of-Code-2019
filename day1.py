import numpy as np

# Advent of Code - Day 1

s1 = 0  # Sum for part 1
s2 = 0  # Sum for part 2

with open('input1.txt', 'r') as f:
    for m in f:
        m = np.floor(int(m)/3) - 2
        s1 += m
        while (int(m) > 0):
            s2 += m
            m = np.floor(int(m)/3) - 2
print(s1)
print(s2)

# Part 1 alt

mass = []
with open('input1.txt', 'r') as f:
    for m in f:
        mass.append(int(m))

mass = np.array(mass)
fuel = np.floor(mass/3) - 2

print(np.sum(fuel))
