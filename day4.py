import numpy as np

start = 264793
stop = 803935

count = 0
count2 = 0

for i in range(start, stop+1):
    if (np.all([int(str(i)[j]) <= int(str(i)[j+1])
               for j in range(len(str(i))-1)]) and
        np.any([int(str(i)[j]) == int(str(i)[j+1])
                for j in range(len(str(i))-1)])):

        two = [int(str(i)[j]) == int(str(i)[j+1])
               for j in range(len(str(i))-1)]

        # need false, true, false in two

        two.append(False)
        done = False
        a = False
        for j in range(len(two)-1):
            if not done:
                b = two[j]
                c = two[j+1]
                if (not a and (b and not c)):
                    count2 += 1
                    done = True
                a = b

        count += 1

print('part 1', count)
print('part 2', count2)
