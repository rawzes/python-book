import math
import random
print(math.pi)
print(random.random())
print(random.choice([1,2,3,4,5]))
print(3.1415*2)

s = 'Spam'
print(s[-1])
print(s[0:3])
print(s[:-1])
print(s[0:len(s)])  #Spam
print("test");
print("test3");
s2 = s + "some text" # s is not changed
print(s2*5)

print(s.find("pa"));  # find offset for substring in sting S
print(s.find("pea")); # returns -1 if string is not found

line = 'aaaa,bbb,cc'
print(line.split(','))
print(line.upper())
print(line.isalpha())

# formatting
a = 'a'
b = 'b'

print('some test for %s and for %s' % (a,b))
print('some test for {0} and for {1}'.format(a,b))
print('some test for {} and for {}'.format(a,b))
print(dir())
print(dir(a))
print(help(a.replace))