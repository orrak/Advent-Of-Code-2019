
import numpy as np

s = 0
with open('input1.txt', 'r') as f:
    for m in f:
        m = np.floor(int(m)/3 - 2)
        while (int(m) > 0):
            s += m
            m = np.floor(int(m)/3 - 2)
print(s)
