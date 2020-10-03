
s = 'test'
print(s[:]) # print whole string
print(s[0:-1]) # print tes
print(s[1]) # e
print(s + "xyz") # concatination testxyz
print("A"*90)
#s[0] = "s"  #str' object does not support item assignment
S = "strawberry"
L = list(S)
print(L)
L[0] = 'Z'
print(''.join(L))  # Ztrawberry
s = ''.join(L)
s = s.replace('rr', 'rrr')
print(s)
line = 'aaa,bbb,ccc'
print(line.split(',')) # разбить по разделителю строку
print(line.upper())
test_string = '''etst
gdf
rt
\ttew'''
print(test_string)
print(line.encode("utf-8"))
print(line.encode("utf-16"))