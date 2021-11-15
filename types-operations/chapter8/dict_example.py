table = {'1992': "Monthy Python",
         '1994': "Holy Graal",
         '1996': 'Cherry Pick',
         '2000': "Holy Graal"}

year = '1992'

for year in table:
    print(year + '\t' + table[year])

# the same as in example below
for year in table.keys():
    print(year + '\t' + table[year])

# dict comprehension

name = "Holy Graal"
print([key for (key, value) in table.items()])  # ['1992', '1994', '1996']

print([key for (key, value) in table.items() if value == name])  # ['1994']
print([key for key in table.keys() if table[key] == name])  # the same

rec = {'name': 'Bob',
       'positions': ['dev', 'qa'],
       'age': 30,
       'address': {'country': 'US', 'zip': '12345'}}

print(rec['positions'][1])
print(rec['address']['country'])
print(rec['address'])

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
print(type(D))

# the same for python 3.x
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {k: k + 1 for k in [1, 2, 3]}  # {1: 2, 2: 3, 3: 4}
print(D)

D1 = dict.fromkeys([1, 2, 3], 0)
# the same
D2 = {k: 0 for k in [1, 2, 3]}
print(D1)  # {1: 0, 2: 0, 3: 0}
print(D2)  # {1: 0, 2: 0, 3: 0}
D3 = dict.fromkeys([1, 2, 3])
print(D3)  # {1: None, 2: None, 3: None

print(type(D.keys()))  # <class 'dict_keys'>  for python3, but for 2.7 is list

for k in D.keys():
    print(k)
# the same
for k in D:
    print(k)


D = {'a': 1, 'b': 2, 'c': 3}
K = D.keys()
V = D.values()
print("Keys: " + str(list(K)))
print("Value: " + str(list(V)))

del D['a']
print("Keys: " + str(list(K)))  # изменения отобразятся во всех представлениях
print("Value: " + str(list(V)))
# result will be following:
'''
Keys: ['a', 'b', 'c']
Value: [1, 2, 3]
Keys: ['b', 'c']
Value: [2, 3]
'''

D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & D)
print(D.keys() & {'b'})
print(D.keys() & {'b': 1})  # the same
print(D.keys() | {'b', 'c', 'd'})