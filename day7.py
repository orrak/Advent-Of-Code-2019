from day5 import test_intcode
import itertools

f = open('input7.txt', 'r').readlines()

lst = f[0].split(',')

seqarr = list(itertools.permutations([0, 1, 2, 3, 4]))

amp = ['A', 'B', 'C', 'D', 'E']
finalsignal = []

for seq in seqarr:
    inp2 = 0
    for i in range(5):
        # make copy of lst that gets changed
        # lst should never change
        tmplst = lst.copy()
        inp1 = seq[i]
        tmplst, outs, index = test_intcode(tmplst, inp1, inp2, False, 0)
        inp2 = outs[0]
        if i == 4:
            finalsignal.append(outs[0])

print('Answer 1', max(finalsignal))

seqarr = list(itertools.permutations([5, 6, 7, 8, 9]))

final = []

for seq in seqarr:
    inp2 = 0

    # save tmplst for each amplifier
    tmplsts = [lst.copy() for i in range(5)]
    # save index for each amplifier
    index = [0 for i in range(5)]

    nodone = True
    first = True

    i = 0
    while nodone:
        if inp2 == 'done':
            nodone = False
        else:
            final.append(inp2)

            if first:
                inp1 = seq[i]
            else:
                inp1 = inp2

            tmplsts[i], inp2, index[i] = test_intcode(tmplsts[i],
                                                      inp1, inp2,
                                                      True, index[i])
            # loop so amp 4 sends output to amp 0
            if i == 4:
                i = 0
                first = False
            else:
                i += 1

print('Answer 2', max(final))
