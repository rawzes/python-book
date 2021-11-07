s = 'spam'

s = s + 'SPAM!'
print(s)
s = s[:4] + 'Burger' + s[-1]
print(s)
s = 'spam' + 'SPAM!'
s = s.replace('SPAM', 'Burger')
print(s)

# string formatting
print('This is %d %s bird' % (1, 'dead'))
print('This is {0} {1} bird'.format(1, 'dead'))

s = 'spam'
result = s.find('pa')
print(result)  # индекс вхождения найденного элемента в подстроке

s = 'xxxxSPAMxxxxSPAMxxxx'
print(s.replace('SPAM', 'TEST'))
print(s.replace('SPAM', 'TEST', 1))  # производит замену указанное количество раз

s = 'spammy'
l = list(s)
l[3] = 'x'
l[4] = 'x'

s = ''.join(l)  # объединяет каждый элемент последовательности с 'a'
print(s)

line = 'aaa bbb ccc '
data = line.split()  # пробел по умолчанию
print(data)
line = 'aaa,bb,ccc'
data = line.split(',')
print(data)
