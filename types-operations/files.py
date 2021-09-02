import struct # for binary data

f = open('test.txt', 'w') # new file will be created
f.write('some text\n')
f.write('another text\n')
f.close() # reset io buffers
# ValueError: I/O operation on closed file.
# print(f.readlines())

f = open('test.txt') # 'r' - default mode
text = f.read()
print(text.split())
f.close()

# another variant via iterators

for line in open('test.txt'):
    print(line)

# write binary files
packed = struct.pack('>i4sh', 7, b'spam', 8)
file = open('test.bin', 'wb')
file.write(packed)
file.close()

# read binary files

data = open('test.bin', 'rb').read()
print(data) # binary data will be
print(list(data))
print(struct.unpack('>i4sh', data))

# setting encoding for supporting all platforms
S = 'sp\xc4m'
file = open('test.txt', 'w', encoding='utf-8')
file.write(S)
file.close()
print(S)
file = open('test.txt', encoding='utf-8')
data = file.read()
file.close()
print(data)

raw = open('test.txt', 'rb').read()
print(raw.decode('utf-8')) # manual decode data in sting
print(data.encode('utf-8')) # manual encode string in bytes