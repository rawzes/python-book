X = set('spam') # creates set from list
Y = {'h', 'a', 'm'}

print(X,Y)

print(X | Y) # объединение
print(X & Y) # пересечение
print(X - Y) # разность
print(X > Y) # надмножество
set1 = {n**2 for n in [1,2,3]}
print({n**2 for n in [1,2,3]})

print(list(set([1,1,3,4,5,5,3,6]))) # использование множеств для фильтрации
print(set('spam') - set('ham'))
print(set('spam') == set('pasm')) # True will be, but 'spam' == 'pasm' - False

print(1/3)