import sys
print(sys.argv)  # returns arguments of command line

s = '1234567890'
print(s[::2])  # 13579
print(s[::-2])  # 08642
s = 'spam'
print(s[1:3])
print(s[slice(1, 3)])
print(s[::-1])
print(s[slice(None, None, -1)])

n = int('35')
string = str(45)
'''
repr() - отображение текст так как он указан в параметре, вместе с кавычками
'''
print(str('test'), repr('test'))  # test 'test'

# преобразование строк в числа и наоборот
s = 42
i = '1'

print(s + int(i))
print(str(s) + i)
print(str(3.1515))
print(float('3.14'))

c = 'c'
b = 120

print(chr(b))  # code to char
print(ord(c))  # char to code

print(int('111001', 2))
print(bin(57))