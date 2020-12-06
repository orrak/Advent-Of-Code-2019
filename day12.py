import re
import numpy as np

with open("input12.txt", "r") as f:
    lst = f.read().strip().split("\n")
    pos = np.array([[int(match) for match in re.findall(r'-?[0-9]+', elem)] for elem in lst], dtype=float)
    # print(pos)

    vel = np.zeros((4,3))
    # print(vel)

    t = 0
    while(t < 10):
        # compare position to calc gravity
        for i in range(len(pos)):
            for j in range(i, len(pos)):
                if i != j:
                    if np.any(pos[i] == pos[j]):
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("pos, i=%d, j=%d" % (i, j))
                    print(pos[i])
                    print(pos[j])
                    print("\n")
                    arr1 = 1*(pos[i] > pos[j])
                    arr2 = -1*(pos[i] < pos[j])
                    arr = arr1 + arr2
                    print("arr1")
                    print(arr1)
                    print("arr2")
                    print(arr2)
                    print("change arr")
                    print(arr)
                    print("before vel, i=%d, j=%d" % (i, j))
                    print(vel[i])
                    print(vel[j])
                    vel[i] -= arr
                    vel[j] += arr
                    print("after vel, i=%d, j=%d" % (i, j))
                    print(vel[i])
                    print(vel[j])
                    print("\n")
                    # print(1*(pos[i] == pos[j]))
                    # print(1*(pos[i] < pos[j]))

        for i in range(len(pos)):
            print("pos, vel, i=%d" % i)
            print(pos[i])
            print(vel[i])
            pos[i] += vel[i]
            print("new pos, i=%d" % i)
            print(pos[i])
            print("\n")

        t += 1

    energy = 0
    for i in range(len(pos)):
        print(pos[i], vel[i])
        energy += sum(pos[i]) * sum(vel[i])

    print(energy)

# part one: 3910 too low, 4708 too low, 5000 too low
