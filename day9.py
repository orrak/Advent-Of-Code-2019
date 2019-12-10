def test_intcode(lst, inp1, inp2, loopmode, index):
    i = 0  # current index
    r = 0  # relative base

    for j in range(len(lst)*10):
        lst.append(0)

    if loopmode:
        i = index

    outs = []
    firstinp = True

    for j in range(len(lst)):
        lst[j] = int(lst[j])

    while i < len(lst):
        code = lst[i]

        par1m = 0
        par2m = 0
        par3m = 0

        code = str(code)
        opcode = int(code[-2:])

        # print(code)

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
            if firstinp:
                inp = inp1
                firstinp = False
            else:
                inp = inp2
            lst[par3] = inp
            i += 2

        elif opcode == 4:
            outs.append(par1)
            i += 2
            if loopmode:
                return lst, par1, i

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
            if loopmode:
                return lst, 'done', i

        else:
            i = len(lst)+1

    return lst, outs, i


if __name__ == '__main__':
    f = open('input9.txt', 'r').readlines()
    lst = f[0].strip().split(',')
    _, out1, _ = test_intcode(lst, 1, 0, False, 0)
    _, out2, _ = test_intcode(lst, 2, 0, False, 0)

    print('Answer 1', out1)
    print('Answer 2', out2)
