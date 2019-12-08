f = open('input8.txt', 'r').readlines()
f = str(f[0].strip())

width = 25
height = 6

layers = []
i = 0
while i < len(f):
    layers.append(f[i:i+width*height])
    i += width*height

# find layer with fewest zeros
zeros = [layer.count('0') for layer in layers]
layer = layers[zeros.index(min(zeros))]

print('Answer 1', layer.count('1') * layer.count('2'))


finalvals = []
for i in range(len(layers[0])):
    val = layers[0][i]
    j = 1
    while val == '2':
        j += 1
        val = layers[j][i]

    if val == '1':
        finalvals.append('O')
    if val == '0':
        finalvals.append(' ')

finalvals = ''.join(finalvals)

print('\nAnswer 2:')
i = 0
while i < len(finalvals):
    print(finalvals[i:i+width])
    i += width
