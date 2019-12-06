# Part 1
def total_orbits(right, left):
    # check no element in right is there multiple times
    for r in right:
        if right.count(r) != 1:
            print(r)

    # each element in right has one direct orbit
    direct_orbits = len(right)

    # find indirect orbits

    step_lst = []

    for i in range(len(right)):
        steps = 0
        n = left[i]
        while (n in right):
            n = left[right.index(n)]
            steps += 1
        step_lst.append(steps)

    indirect_orbits = sum(step_lst)

    # answer
    return direct_orbits + indirect_orbits


# read file
f = open('input6.txt', 'r').readlines()

# make right and left lists
right = []
left = []

for i in range(len(f)):
    f[i] = f[i].strip()
    f[i] = f[i].split(')')
    left.append(f[i][0])
    right.append(f[i][1])

print(total_orbits(right, left))


# Part 2
def find_santa(current, steps):
    path.append(current)
    # print(current, steps)
    # done
    if current == 'SAN':
        print(steps)
    # move left
    # print('try move left', current)
    if current in right and left[right.index(current)] not in path:
        # print('move left')
        new_current = left[right.index(current)]
        find_santa(new_current, steps+1)
    # move right
    # print('try move right', current)
    if current in left:
        lst = [i for i in range(len(left)) if left[i] == current]
        for index in lst:
            if right[index] not in path:
                # print('move right')
                new_current = right[index]
                find_santa(new_current, steps+1)
    path.remove(current)


start = 'YOU'
steps = 0
path = []

find_santa('YOU', 0)
