
int(3.14) # 3
float(5) # 5.0
a = 3
b = 4

print(a+1, a-1) # a, b will not changed
print(b*3, b / 2)
print(a%2, b**2)
d = a%2, b**2
print(type(d)) # tumple will be

# error will be: 'c' is not defined
# c * 2

print(b / (2 + a)) # 0.80000000000000004
num = 1/3
print(num)
print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))
print(repr('test')) # outpus as is in code
print('test') # user-friendly output

print(1<2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 5

print(X<Y<Z)
print(X<Y and Y<Z)

print(1.1+2.2 == 3.3) # false
print(int(1.1+2.2) == int(3.3)) # true