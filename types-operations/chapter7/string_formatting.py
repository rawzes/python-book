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
