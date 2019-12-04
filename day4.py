import numpy as np

# range from input
start = 264793
stop = 803935

# counters for part 1 and part 2
count = 0
count2 = 0

for i in range(start, stop+1):
    # if digits never decrease and two adjacent digits are the same
    if (np.all([int(str(i)[j]) <= int(str(i)[j+1])
               for j in range(len(str(i))-1)]) and
        np.any([int(str(i)[j]) == int(str(i)[j+1])
                for j in range(len(str(i))-1)])):

        # array of where adjacent digits are the same
        two = [int(str(i)[j]) == int(str(i)[j+1])
               for j in range(len(str(i))-1)]

        # for part 2:
        # need a true not next to another true in two
        # then there is a group of two matching digits that
        # are not part of a larger group

        # put in False at first and last place
        # to catch a True at the ends of the array
        two.append(False)
        two.insert(0, False)

        # if there is a two group
        if (np.any([not two[j] and (two[j+1] and not two[j+2])
                    for j in range(len(two)-2)])):
            count2 += 1

        count += 1

print('part 1', count)
print('part 2', count2)
