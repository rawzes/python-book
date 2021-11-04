
path = r'D:\DATA'
print(path)

'''
a = 3
многострочный комментарий
'''

print(len('213')) # 3
print('abc' + 'dfg') # concatenation
print('test' * 4) # повторение, тоже что и 'test' + 'test' ...
print('-' * 80)

myjob = 'tester'
for c in myjob:
    print(c, end='\t')
print('\n')
print('z' in myjob)
print('t' in myjob)

s = 'spam'
print(s[0], s[-2])
print(s[1:3]) # pa
print(s[:3]) # spa
print(s[1:]) # pam
print(s[1:-2]) # p len(s)+ (-2) = 2 - number index