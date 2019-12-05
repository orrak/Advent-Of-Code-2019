def func(lst):
    i = 0
    outs = []

    for j in range(len(lst)):
        lst[j] = int(lst[j])

    while i < len(lst):
        code = lst[i]

        par1m = 0
        par2m = 0

        code = str(code)
        opcode = int(code[-2:])

        if len(code) >= 3:
            par1m = int(code[-3])

        if len(code) >= 4:
            par2m = int(code[-4])

        if opcode in [1, 2, 3, 4, 5, 6, 7, 8]:
            if par1m:
                par1 = lst[i+1]
            else:
                par1 = lst[lst[i+1]]

        if opcode in [1, 2, 5, 6, 7, 8]:
            if par2m:
                par2 = lst[i+2]
            else:
                par2 = lst[lst[i+2]]

        if opcode in [1, 2, 7, 8]:
            par3 = lst[i+3]

        if opcode == 1:
            lst[par3] = par1 + par2
            i += 4

        elif opcode == 2:
            lst[par3] = par1*par2
            i += 4

        elif opcode == 3:
            inp = int(input('provide input: '))
            pos = lst[i+1]
            lst[pos] = inp
            i += 2

        elif opcode == 4:
            outs.append(par1)
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

        elif opcode == 99:
            i = len(lst)+1

        else:
            print('fail, opcode =', opcode)
            i = len(lst)+1

    return lst, outs


f = open('input5.txt', 'r').readlines()
lst = f[0].split(',')

# lst = '3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9'
# lst = lst.split(',')

lst, outs = func(lst)
print(outs)
