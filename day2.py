def func(lst):
    i = 0
    while i < len(lst):
        if lst[i] == 1:
            lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
            i += 4
        elif lst[i] == 2:
            lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
            i += 4
        elif lst[i] == 99:
            i = len(lst)+1
        else:
            i = len(lst)+1
    return lst


# Part 1
f = open('input2.txt', 'r').readlines()
lst = f[0].split(',')
lst[1] = 12
lst[2] = 2

for i in range(len(lst)):
    lst[i] = int(lst[i])

lst = func(lst)

print(lst[0])

# Part 2
for noun in range(100):
    for verb in range(100):

        f = open('input2.txt', 'r').readlines()
        lst = f[0].split(',')

        lst[1] = noun
        lst[2] = verb

        for i in range(len(lst)):
            lst[i] = int(lst[i])

        lst = func(lst)

        if lst[0] == 19690720:
            print(100*noun + verb)
