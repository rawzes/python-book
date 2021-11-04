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
