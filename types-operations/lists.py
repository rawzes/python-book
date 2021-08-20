'''
Список - упорядоченная коллекция объектов производльных типов
'''
list2 = ['test', 3.14, 5]
print(type(list2))
print(len(list2))
'''
Поддержка всех операций над последовательностями, подобно строкам
'''
'''Списки могут быть вложенными'''
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)
print(M[0])
print(M[1][1])
'''Списковые включения''' # list comprehension
col2 = [row[1]+2 for row in M]
print(col2)
'''Отфильтровать нечетные элементы в списке'''
print([r[0] for r in M if r[0] % 2 == 1])  # [1,7]
diag = [M[i][i] for i in [0,1,2]]
print(diag)
'''Генерация списка элементов с помощью range'''
list_range = list(range(1, 10, 2))
print(list_range) #1,3,5,7,9

L = [1,2,4,"5"]
L.append("test") # add item to the end
print(L)
L.pop(1) # select item by offset
print(L)
M = ['bb', 'a', 'z']
M.sort()
print(M)
M.reverse()
print(M)

