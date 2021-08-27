for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('test!'*x)
    x-=1

sqr1 = [x**2 for x in [1,2,3,4,5]]
sqr2 = []
for x in [1,2,3,4,5]:
    sqr2.append(x**2)
print(sqr1)
print(sqr2)