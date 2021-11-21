import pickle
# pickle - more safe way to load object from file, intended for serialization \ deserialization objects
D = {'a': 1, 'b': 'test', 'c': 'some text'}

F = open('test1.bin', 'wb')
pickle.dump(D, F)
print('data has been written')
F.close()

F = open('test1.bin', 'rb')
some_variable = pickle.load(F)
F.close()
print(some_variable)
