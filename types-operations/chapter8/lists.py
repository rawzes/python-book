s = help(list)
print(s)

L = []  # пустой список
L = [1, 3, "test", {}]  # 4 элемента
L = [1, 3, 'test2', ['e1', 'e2']]  # вложенные подсписки
print(L[3][0])  # e1

'''
Генерация списков из итерируемых объектов
'''
L = list('spam')
L = list(range(-10, 10))
print(len(L))  # 20
print(L)  # [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[4])  # -6
print(L[5:10])  # [-5, -4, -3, -2, -1]

L2 = L + ['new1']  # concatination
L3 = L2 * 10  # повторение
print(L2)
print(L3)

L.append(5)
L.sort()
L.reverse()
print(L.count(5))
L.extend([5, 5])
print(L.count(5))  # 4
L.copy()
print(L)
L.clear()
print(L)  # []

print(list(map(abs, [-3, 3])))  # [3, 3]


L = ['spam', 'eggs', 'SPAM!']
L[1] = ('eat')
print(L)  # ['spam', 'eat', 'SPAM!']
L[1:2] = ['test1']
print(L)  # ['spam', 'test1', 'SPAM!']
L[0:2] = ['eat', 'more']
print(L)  # ['eat', 'more', 'SPAM!']
print(L[1:2])

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)  # [1, 4, 5, 3]
L[1:1] = [7, 8]
print(L)  # [1, 7, 8, 4, 5, 3]
L[1:2] = []
print(L)  # [1, 8, 4, 5, 3]
L[1:1] = []
print(L)  # [1, 8, 4, 5, 3]


L = [1]
L[:0] = [2, 3, 4]  # insert list in first position
print(L)  # [2, 3, 4, 1]
L[len(L):] = [5, 6, 7]  # insert list at the end
print(L)  # [2, 3, 4, 1, 5, 6, 7]
L.extend([8, 9, 10])
print(L)  # [2, 3, 4, 1, 5, 6, 7, 8, 9, 10]
L.append(11)
print(L)  # [2, 3, 4, 1, 5, 6, 7, 8, 9, 10, 11]

#print([1, 2, 'test'].sort())  # TypeError: '<' not supported between instances of 'str' and 'int'
print(sorted(L, reverse=True))  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(L.pop())  # 11 - last element will be deleted and returned
print(L)  # [2, 3, 4, 1, 5, 6, 7, 8, 9, 10]

'''
L.extend() - adds many arguments
L.append() - adds one argument
'''

print(L.index(10)) # 9
L.insert(10, 'test')
print(L)
L.remove('test')  # remove by value
print(L)
print(L.count(8))  # 1

g = 45

print(2**32 / 1024)
print(2**64)