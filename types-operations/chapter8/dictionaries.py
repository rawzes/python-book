D = {'name': 'Roma', 'age': 29}
print(D.values())  # dict_values(['Roma', 29])
print(D.keys())  # dict_keys(['name', 'age'])
print(list(D.keys()))  # ['name', 'age']

print(D['age'])  # 29

s = D.pop('age')  # select by key + delete from source dict
print(str(D) + '\t' + str(s))

D.update({'age': 30})
print(len(D))  # 2
print(D)  # {'name': 'Roma', 'age': 30}

D['age'] = 100
print(D)
D['new'] = 'some value'  # new key + value will be added
print(str(D) + "\t length: " + str(len(D)))

D = {'Eggs': 2, 'Spam': 1, 'Ham': 2}

D['Ham'] = ['meat', 'milk', 'solt']
print(D)  # {'Eggs': 2, 'Spam': 1, 'Ham': ['meat', 'milk', 'solt']}
print(D['Ham'][1])  # milk
del D['Spam']
print(len(D))
D['money'] = 123.45
print(D)
print(list(D.items()))  # [('Eggs', 2), ('Ham', ['meat', 'milk', 'solt']), ('money', 123.45)]

print(D.get('Eggs'))  # 2
print(D.get('test'))  # None
print(D.get('test', 100))  # default value will be returned