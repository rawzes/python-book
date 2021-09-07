import decimal
import math
import random
from decimal import Decimal
x = 1 # 01
x = x << 2 # shift left on 2 bits 0100
print(x) # 4
print(x | 2) # byte OR
print(x & 1) # byte AND

x = 0xFF
print(bin(x))
print(x ^ 0b10101010) # 85
print(bin(x ^ 0b10101010)) 
print(int('0b1010101', 2)) # 85
print(hex(85)) # 0x55
print(math.pi)
print(math.e)

print(2**4, pow(2,4))
print(abs(-10.4), max(1,2,6,7), sum((1,2,3)))

x = 2.567
x2 = -2.567
print(math.floor(x), math.floor(x2)) # округление до ближайжешего меньшего целого числа
print(math.trunc(x), math.trunc(x2)) # усечение
print(int(x), int(x2)) # 2, -2
print(round(x), round(x2), round(x, 2)) # 3 -3 2.57
print('%.1f' % x, '{0:.2f}'.format(x)) # 2.6 2.57

print(144 ** .5, pow(144, .5), math.sqrt(144)) # 12.0 12.0 12.0
print(random.random(), random.random())
print(random.randint(1,100))
l = ['test1', 'test2', 'test3']
print(random.choice(l))
random.shuffle(l)
print(l)
random.shuffle(l)
print(l)

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal(1) / Decimal(7))
decimal.getcontext().prec = 3
print(Decimal(1) / Decimal(7))