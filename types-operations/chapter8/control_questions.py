# create a list with 5 zeros
L = [0, 0, 0, 0, 0]
L = [0] * 5
L = [0 for x in range(5)]

# create a dict with { 'a': 0, 'b': 0, 'c': 0 }
D = {'a': 0, 'b': 0, 'c': 0}
D = dict(a=0, b=0, c=0)
D = dict.fromkeys('ab', 0)
D = {k: 0 for k in 'abc'}
D = {}
D['a'] = 0
D['b'] = 0
D['c'] = 0
D = dict([('a', 0), ('b', 0), ('c', 0)])
