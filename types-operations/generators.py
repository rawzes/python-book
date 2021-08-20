M = [[1,2,3], [4,5,6], [6,7,8]]
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))
# print(next(G)) will be error on next attempt: StopIteration