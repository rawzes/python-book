import math
print(math.floor(-2.5)) # -3
print(math.floor(2.5)) # 2
print(math.trunc(-2.5)) # -2
print(math.trunc(2.5)) # 2

print(5 / 2, 5 / -2)
print(5 //2, 5 // -2) # 2 -3

print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)
print(0o1, 0o71) # 1 57
print(0x01, 0xFF)# 1 255
print(0b1, 0b11111111) # 1 255

print(bin(64), oct(64), hex(64))

print(eval('0xFF')) # runs code inside as-is

print('{0:b}, {1:x}, {2:o}'.format(64,64,64)) # only numbers are displayed
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(bin(n))
print(n)