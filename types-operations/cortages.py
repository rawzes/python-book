T = (1, 2, 3, 4, 5, 5)
T += (5, 6)
print(T)
test = T[0]
print(test, 'length = ', len(T))
print(T.index(1)) # get first index of 1 value
print(T.count(5)) # get count of 5 value in tuple