L = ['test']
L.append(L)

print(L)  # ['test', [...]]

X = 'x'
Y = 'y'

X, Y = Y, X

print('x: {}, y: {}'.format(X, Y))
