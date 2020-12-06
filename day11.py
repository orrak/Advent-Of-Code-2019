from day9 import test_intcode


def test_intcode_day9(lst):
    i = 0  # current index
    r = 0  # relative base

    for j in range(len(lst)*10):
        lst.append(0)

    outs = []

    outcolor = True  # first output is color
    panelcolors = {}
    currentpanel = [0, 0]
    direction = 0  # up
    painted = {}

    dirs = ['up', 'right', 'down', 'left']

    panelcolors[tuple(currentpanel)] = 0

    for j in range(len(lst)):
        lst[j] = int(lst[j])

    count = 0
    while i < len(lst) and count > -1:
        count += 1

        code = lst[i]

        # print(code)

        par1m = 0
        par2m = 0
        par3m = 0

        code = str(code)
        opcode = int(code[-2:])

        # print('code', code)

        if len(code) >= 3:
            par1m = int(code[-3])

        if len(code) >= 4:
            par2m = int(code[-4])

        if len(code) >= 5:
            par3m = int(code[-5])

        if opcode in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if par1m == 1:
                par1 = lst[i+1]
            elif par1m == 2:
                par1 = lst[lst[i+1] + r]
            else:
                par1 = lst[lst[i+1]]

        if opcode in [1, 2, 5, 6, 7, 8]:
            if par2m == 1:
                par2 = lst[i+2]
            elif par2m == 2:
                par2 = lst[lst[i+2] + r]
            else:
                par2 = lst[lst[i+2]]

        if opcode in [1, 2, 3, 7, 8]:
            if par3m == 0:
                par3 = lst[i+3]
            elif par3m == 2:
                par3 = lst[i+3] + r

        if opcode == 1:
            lst[par3] = par1 + par2
            i += 4

        elif opcode == 2:
            lst[par3] = par1*par2
            i += 4

        elif opcode == 3:
            # 0 if black panel, 1 if white panel
            # print('--opcode 3, input')
            # print('current panel', tuple(currentpanel))
            # print('color', panelcolors[tuple(currentpanel)])
            inp = panelcolors[tuple(currentpanel)]
            '''
            if inp == 1:
                print('current panel', currentpanel)
                input('stop')
            '''
            # print('inp', inp)
            inp = int(input('give input '))
            lst[par3] = inp

            i += 2

        elif opcode == 4:
            # print('----', par1, '----')
            # print('output', par1)
            outs.append(par1)
            # print('--opcode 4, output', par1)
            # print('current panel', tuple(currentpanel))

            if outcolor:
                # print('paint', tuple(currentpanel), par1)
                panelcolors[tuple(currentpanel)] = par1
                painted[tuple(currentpanel)] = par1
                # next output will be a turn
                outcolor = False
            else:
                # print('current direction', dirs[direction])
                # directions: 0 = up, 1 = right, 2 = down, 3 = left
                # turn: par1 = 0, turn left, par1 = 1, turn right

                # turn
                if par1 == 0:
                    direction -= 1
                    if direction == -1:
                        direction = 3
                elif par1 == 1:
                    direction += 1
                    if direction == 4:
                        direction = 0

                # move
                if direction == 0:
                    currentpanel[0] += 1
                elif direction == 1:
                    currentpanel[1] += 1
                elif direction == 2:
                    currentpanel[0] -= 1
                elif direction == 3:
                    currentpanel[1] -= 1

                print('new direction', dirs[direction])
                # print('new panel', tuple(currentpanel))

                # all panels begin as black
                # if we have moved to a panel we have not been at before
                # we know it is black
                if tuple(currentpanel) not in panelcolors.keys():
                    panelcolors[tuple(currentpanel)] = 0

                # next output will be a color
                outcolor = True

            i += 2

        elif opcode == 5:
            if par1:
                i = par2
            else:
                i += 3

        elif opcode == 6:
            if par1 == 0:
                i = par2
            else:
                i += 3

        elif opcode == 7:
            if par1 < par2:
                lst[par3] = 1
            else:
                lst[par3] = 0
            i += 4

        elif opcode == 8:
            if par1 == par2:
                lst[par3] = 1
            else:
                lst[par3] = 0
            i += 4

        elif opcode == 9:
            r += par1
            i += 2

        elif opcode == 99:
            i = len(lst)+1
            print('--opcode 99--')

        else:
            print('failed')
            i = len(lst)+1

    return lst, outs, i, painted, panelcolors


if __name__ == '__main__':
    f = open('input11.txt', 'r').readlines()
    f = f[0]
    f = f.strip()
    lst = f.split(',')

    for i in range(len(lst)):
        lst[i] = int(lst[i])

    for i in range(len(lst)*10):
        lst.append(0)

    panelcolors = {}
    currentpanel = [0, 0]
    direction = 0  # up
    painted = {}

    dirs = ['up', 'right', 'down', 'left']

    panelcolors[tuple(currentpanel)] = 0

    i = 0

    done = False
    count = 0
    while not done and count < 20:
        count += 1
        print('-------------------------')
        print('current panel', currentpanel)
        print('color', panelcolors[tuple(currentpanel)])

        inp = panelcolors[tuple(currentpanel)]

        # print('inp', inp)

        lst, out1, i = test_intcode(lst, inp, True, i)
        lst, out2, i = test_intcode(lst, inp, True, i)

        print('out', out1, out2)

        if out1 == 'done' or out2 == 'done':
            done = True
            break

        # color
        panelcolors[tuple(currentpanel)] = out1
        painted[tuple(currentpanel)] = out1

        # turn
        if out2 == 0:
            direction -= 1
            if direction == -1:
                direction = 3
        elif out2 == 1:
            direction += 1
            if direction == 4:
                direction = 0

        # move
        if direction == 0:
            currentpanel[0] += 1
        elif direction == 1:
            currentpanel[1] += 1
        elif direction == 2:
            currentpanel[0] -= 1
        elif direction == 3:
            currentpanel[1] -= 1

        # print('new direction', dirs[direction])
        # print('new panel', tuple(currentpanel))

        # all panels begin as black
        # if we have moved to a panel we have not been at before
        # we know it is black
        if tuple(currentpanel) not in panelcolors.keys():
            panelcolors[tuple(currentpanel)] = 0

        print('current panel', currentpanel)
        print('color', panelcolors[tuple(currentpanel)])

    # lst, outs, i, painted, panelcolors = test_intcode_day9(lst)

    print(panelcolors)
    print(len(painted.keys()))

    # wrong answers part 1: 6, 14, 17
