x = set('abcdef')
y = set('defxyz')

print(x, y)

print(x - y)
print(x | y)
print(x ^ y)
print(x & y)
print(x>y, x<y)
print('x' in y, 10 in [1,2,0,10]) # works for strings, list, sets

z = x.intersection(y)
print(z)
z.add('SPAM')
print(z)
z.update(set(['X', 'Y']))
print(z)
z.remove('e')
print(z)

for item in z:
    print(item*3)

S = set([1,2,3,4])
S | set([4,5])
# S | [4,5] # TypeError: unsupported operand type(s) for |: 'set' and 'list'
print(S.union([5,6]))
print(S.intersection((5,6)))
print(S.issubset(range(-1, 10)))

S1 = {1,2,3,4}
print(S1 - {1,2,3,4}) # set()
print(type({})) # <class 'dict'>
S2 = set() # empty set
# TypeError: unhashable type: 'list'
# S2.add([1,2,3])
# S2.add(['a': 1])
S2.add((1,2,3,4))

S  = { x**2 for x in [1,2,3,4]}
print(S)

S = { x for x in 'SPAM'} # the same as set('SPAM')
print(S)

# common usecases
L = [1,2,3,1,2,5,6]
print(list(set(L))) # duplicates will be deleted
print(set([1,2,4,5,6,7]) - set([1,2,7,8])) # 4,5,6 - diff
print(set('spam') - set('arm')) # p,s
print(dir(bytes))

L1, L2 = [1,4,3,2,5], [1,2,3,4,5]
print(L1 == L2) # false
print(set(L1) == set(L2)) # true проверка на равенство нейтральное к порядку элементов списка
print(sorted(L1) == sorted(L2))

# real example how to use sets
engineers = {'bob', 'tom', 'roma'}
qa = {'roma', 'max', 'sasha'}
print('roma' in engineers)
print(engineers & qa)