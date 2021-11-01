from typing import List


print(1>2, 2>1)

print([None]*100)
print(type (None))
print(type(type(None)))

# how to check types
L = [1,2,3]
#1 variant
if type([]) == type(L):
    print('yes')

#2 variant
if type([]) == list:
    print('yes')

#3 variant
if isinstance(L, list):
    print('yes')