from decimal import Decimal, localcontext
import decimal
from fractions import Fraction
print(decimal.Decimal(1) / decimal.Decimal(7))

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(7))

print(decimal.Decimal(1) / decimal.Decimal(7))

x = Fraction(1,3)
y = Fraction(4,6)

print(x, y)
print(x+y)
print(x-y)
print(x*y)

print((2.5).as_integer_ratio()) # (5,2)
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)

print(float(z + 1)) 

print(Fraction.from_float(2.5)+2.0) # Fraction + float -> float
# Fraction + int -> Fraction

