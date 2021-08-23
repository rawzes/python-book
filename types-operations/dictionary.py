D = {'food': 'Milk', 'quantity': 4, 'color': 'red'}
D['quantity'] +=2
print(D['food'], D['quantity'])

D = {}
D['name'] = 'Roma'  # new key will be created
D['age'] = 29
D['job'] = 'QA'
print(D)

emp1 = dict(name='Bob', age=40, position='qa')
print(emp1)
emp2 = dict(zip(['name', 'age', 'position'], ['Nick', 50, 'dev']))
print(emp2)

emp3 = {'name': {'first': 'Dima', 'last': 'Ivanov'}, 'jobs': ['qa', 'dev'], 'age': 40.5}
print(emp3)
print(emp3['name']['last'])
rec1 = emp3['jobs']
print(rec1, type (rec1))

emp3['jobs'].append('junitors') # extending list with new value
print(emp3)

emp3 = '' # all memory will be deleted automatically
print('f' in emp3) # checking if ley 'f' is present in emp3
if not 'f' in emp3:
    print('error.... key is not found')