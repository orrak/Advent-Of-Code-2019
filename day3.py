def get_coords(wire):
    coords = [(0, 0)]
    x, y = 0, 0

    for i in wire:
        d = i[0]
        n = int(i[1:])
        if d == 'R':
            for i in range(x+1, x+n+1):
                coords.append((i, y))
            x += n
        if d == 'L':
            for i in range(x-1, x-n-1, -1):
                coords.append((i, y))
            x -= n
        if d == 'U':
            for i in range(y+1, y+n+1):
                coords.append((x, i))
            y += n
        if d == 'D':
            for i in range(y-1, y-n-1, -1):
                coords.append((x, i))
            y -= n

    return coords


# read wires
f = open('input3.txt', 'r').readlines()
wire1 = f[0].split(',')
wire2 = f[1].split(',')

# get lists of coordinates
coords1 = get_coords(wire1)
coords2 = get_coords(wire2)

# find points where wires cross
intsec = list(set(coords1).intersection(coords2))

# find minimum steps
s = []
for e in intsec:
    s1 = coords1.index(e)
    s2 = coords2.index(e)
    s.append(s1 + s2)

s.remove(0)
print('minimum steps', min(s))

# find minimum distance
dist = []
for e in intsec:
    dist.append(abs(e[0]) + abs(e[1]))

dist.remove(0)
print('minimum distance', min(dist))
