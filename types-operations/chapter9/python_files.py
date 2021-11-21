x, y, z = 44, 45, 46
L = [1, 2, 4]
D = {'a': 1, 'b': 2, 'c': 3}

file = open('test_file.txt', 'w')
file.write('%s, %s, %s\n' % (x, y, z))
file.write('%s & %s\n' % (L, D))
file.close()

file = open('test_file.txt')

line = file.readline().rstrip()
list_numbers = line.split(',')
x, y, z = list_numbers
print('Values from file: x = %s, y = %s, z = %s\n' % (x, y, z))
data = file.readline().split('&')
parts = [eval(p) for p in data]  # eval() - reads text as python code
print(parts)
L = parts[0]
D = parts[1]
print('Values from file: L = %s, D = %s\n' % (L, D))
file.close()

