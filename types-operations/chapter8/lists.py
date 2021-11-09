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
