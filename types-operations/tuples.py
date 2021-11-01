T = (1, 2, 3, 4, 5, 5)
T += (5, 6)
print(T)
test = T[0]
print(test, 'length = ', len(T))
print(T.index(1)) # get first index of 1 value
print(T.count(5)) # get count of 5 value in tuple

# tuples are not changable
# TypeError: 'tuple' object does not support item assignment
# T[0] = 2
T = (3.15,) + T[1:]  # new tuple will be created
print(T)

T = 3.14, 'test', [1,2,3] # tuple will be created
print(T)