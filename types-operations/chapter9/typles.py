T = (1,) + (2,3)
print(T)
print(type(T))  #<class 'tuple'>

T = T[0], T[1:2], T * 3  # (1, (2,), (1, 2, 3, 1, 2, 3, 1, 2, 3))
print(T)

# sorting is not available

T = ('aa', 'cc', 'dd', 'bb')
tmp = list(T)
tmp.sort()
T = tuple(tmp)
print(T)

# or sorted(T)
T = ('aa', 'cc', 'dd', 'bb')
T = sorted(T)  # ['aa', 'bb', 'cc', 'dd']
print(T)

T = 1, 2, 3, 4, 5
L = [x + 100 for x in T]
print(L)  # [101, 102, 103, 104, 105]

T = 1, 2, 2, 3, 4, 2, 5
print(T.count(2))  # 3
print(T.index(2))  # 1
print(T.index(2, 3))  # 5

T = (1, [2, 3], 4)
# T[0] = 'test' - error
T[1].append('test')
print(T)  # (1, [2, 3, 'test'], 4)

