import math


def count_asteroids(f, fx, fy, countarr):
    # count number of asteriods visible from
    # position fx, fy
    ast = 0  # number of visible asteroids

    # print('start asteroid', fx, fy)

    for x in range(len(f)):
        for y in range(len(f[0])):
            if f[x][y] == '#' and (fx != x or fy != y):
                # print('current asteroid', x, y)

                xstep = x-fx
                ystep = y-fy

                m = min(abs(xstep), abs(ystep))
                gcd = 0
                for z in range(1, m+1):
                    if xstep % z == 0 and ystep % z == 0 and z > gcd:
                        gcd = z

                if gcd > 0:
                    xstep = int(xstep/gcd)
                    ystep = int(ystep/gcd)

                if xstep == 0:
                    ystep = int(ystep/abs(ystep))

                if ystep == 0:
                    xstep = int(xstep/abs(xstep))

                currx = fx + xstep
                curry = fy + ystep
                block = False
                done = False

                # check if there is an asteriod blocking x, y
                # from being visible from fx, fy
                while (not block and not done and 0 <= currx < len(f)
                       and 0 <= curry < len(f[0])):
                    if f[currx][curry] == '#':
                        # print('hit', currx, curry)
                        done = True
                        block = True
                    if currx == x and curry == y:
                        done = True
                        block = False
                    currx += xstep
                    curry += ystep

                if not block and f[x][y] == '#':
                    ast += 1

    # print('total visible from', fx, fy, 'is', ast)
    countarr[fx][fy] = ast

    return countarr


def calc_angle_and_dist(start, end):
    distance = math.sqrt(abs(start[0] - end[0])**2
                         + abs(start[1] - end[1])**2)
    angle = 0

    if end[0] < start[0] and end[1] >= start[1]:
        angle = math.asin(abs(start[1]-end[1])/distance)

    if end[0] >= start[0] and end[1] > start[1]:
        angle = math.asin(abs(start[0]-end[0])/distance)
        angle = angle + math.pi/2

    if end[0] > start[0] and end[1] <= start[1]:
        angle = math.asin(abs(start[1]-end[1])/distance)
        angle = angle + math.pi

    if end[0] <= start[0] and end[1] < start[1]:
        angle = math.asin(abs(start[0]-end[0])/distance)
        angle = angle + 3*math.pi/2

    angle = round(angle, 5)  # round off angle

    return distance, angle


if __name__ == '__main__':
    # read file
    f = open('input10.txt', 'r').readlines()
    f = [e.strip() for e in f]

    # make variables
    countarr = [[0 for i in range(len(f[0]))] for i in range(len(f))]
    astcount = 0

    # count visible asteroids
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == '#':
                astcount += 1
                countarr = count_asteroids(f, i, j, countarr)

    # find max visible asteroids
    m = [max(countarr[i]) for i in range(len(countarr))]
    m = max(m)
    print('Answer 1', m)

    # find coords for monitoring station (and laser)
    stationcoords = 0
    for i in range(len(countarr)):
        for j in range(len(countarr[0])):
            if countarr[i][j] == m:
                s = f[i]
                s = [s[i] for i in range(len(s))]
                s[j] = 'L'
                s = ''.join(s)
                f[i] = s
                stationcoords = (i, j)

    lst = []

    # calculate angle and distance from laser to each other asteroid
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == '#' and (i, j) != stationcoords:
                d, a = calc_angle_and_dist(stationcoords, (i, j))
                lst.append((a, d, i, j))

    # sort list by angle
    lst = sorted(lst, key=lambda tup: tup[0])
    angles = [e[0] for e in lst]
    angles = list(dict.fromkeys(angles))

    # sort sublists by distance
    data = []
    for a in angles:
        data.append(sorted([e for e in lst if e[0] == a],
                           key=lambda tup: tup[1]))

    i = 0
    done = False

    num = 0
    # start at angle 0, remove asteroid with lowest distance,
    # go too next angle, remove asteroid with lowest distance,
    # continue untill all asteroids are removed
    while not done:
        if len(data[i]) != 0:
            data[i].reverse()

            num += 1
            ast = data[i].pop()

            if num == 200:
                print('Answer 2', ast[3]*100 + ast[2])

            data[i].reverse()

        if i == len(data)-1:
            i = 0
        else:
            i += 1

        done = True
        for j in range(len(data)):
            if len(data[j]) > 0:
                done = False
