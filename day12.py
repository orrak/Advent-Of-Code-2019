import re
import numpy as np
import math

def calcvel(pos, vel):
    for i in range(len(pos)):
        for j in range(i, len(pos)):
            if i != j:
                arr1 = 1*(pos[i] > pos[j])
                arr2 = -1*(pos[i] < pos[j])
                arr = arr1 + arr2
                vel[i] -= arr
                vel[j] += arr
    return pos, vel

def checkdone(prevpos, pos, prevvel, vel, done):
    posmatch = False
    velmatch = False
    for elem in prevpos:
        if np.all(elem == pos):
            posmatch = True
    for elem in prevvel:
        if np.all(elem == vel):
            velmatch = True

    if posmatch and velmatch:
        done = True
        print("t=%d" % t)

    return prevpos, pos, prevvel, vel, done

def calcenergy(pos, vel):
    t = 0
    while(t < 1000):
        pos, vel = calcvel(pos, vel)
        for i in range(len(pos)):
            pos[i] += vel[i]

        t += 1
    energy = 0
    for i in range(len(pos)):
        energy += (sum(abs(pos[i])) * sum(abs(vel[i])))
    return energy

def calccycle(pos, vel):
    done = False
    startpos = pos.copy()
    startvel = vel.copy()
    t = 0
    while(not done):
        pos, vel = calcvel(pos, vel)
        for i in range(len(pos)):
            pos[i] += vel[i]

        t += 1
        if np.all(startpos == pos) and np.all(startvel == vel):
            done = True
            return t

with open("input12.txt", "r") as f:
    lst = f.read().strip().split("\n")
    pos = np.array([[int(match) for match in re.findall(r'-?[0-9]+', elem)] for elem in lst], dtype=float)
    vel = np.zeros((4,3))

    energy = calcenergy(pos, vel)

    print("part one: %d" % energy)


with open("input12.txt", "r") as f:
    lst = f.read().strip().split("\n")
    pos = np.array([[int(match) for match in re.findall(r'-?[0-9]+', elem)] for elem in lst], dtype=float)
    vel = np.zeros((4,3))

    ts = []
    for i in range(pos.shape[1]):
        lstpos = [m[i] for m in pos]
        lstvel = [m[i] for m in vel]
        t = calccycle(lstpos, lstvel)
        ts.append(t)

    print("part two: %d" % np.lcm.reduce(ts))
