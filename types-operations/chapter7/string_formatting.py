import sys

n = 1234
print('%d %-9d %06d' % (n, n, n))

x = 1.23456789
print('%f, %g, %e, %s' % (x, x, x, x))  # 1.234568, 1.23457, 1.234568e+00, 1.23456789

print('%f...%.2f...%.*f' % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))

data = {'name': 'Roma', 'age': 29}
template = '''
Hi, your name is %(name)s and your age is %(age)d
'''
print(template % data)
print(vars())  # вывод всех переменных существующих на момент вызова
name = 'Roma'
age = 29
print(template % vars())

'''
Formating methods
'''

template = '{0}, {1} and {2}'
print(template.format('Spam', 'Ham', 'Eggs'))

template = '{}, {} and {}'
print(template.format('Spam', 'Ham', 'Eggs'))

template = '{0}, {food} and {1}'
print(template.format('Spam', 'Eggs', food='Ham'))  # сначала позиционные, потом по ключу

# тоже через выражение форматирования

template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='Spam', pork='Ham', food='Eggs'))

template = '{motto}, {0}, and {food}'
print(template.format(43, motto='Spam', food='Myaso'))

# additional parameters
print('My {1[kind]} runs on {0.platform}'.format(sys, dict(kind='PC')))
# or
print('My {1[kind]} runs on {0.platform}'.format(sys, {'kind': 'PC'}))

print('My {type[kind]} runs on {platform.platform}'.format(platform=sys, type={'kind': 'PC'}))


somelist = list('Spam')
print(somelist)
print('First: {0[0]} and Third: {0[2]}'.format(somelist))
print('First: {0} and last: {1}'.format(somelist[0], somelist[-1]))  # указать в строке -1 нельзя

parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)
print(*parts)
print('First: {0}, Last: {1}, Middle: {2}'.format(*parts))

print('{0:10} = {1:10}'.format('spam', 1.2345678))
print('{0:>10} = {1:<10}'.format('spam', 1.2345678))


'''
data = dict(type='test1', type2='test2')
**data = key='value' - распаковывает словарь
'''

print('{0:,d}'.format(999999999999)) # 999,999,999,999

