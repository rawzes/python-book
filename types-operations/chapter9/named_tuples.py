from collections import namedtuple

Rec = namedtuple('Re', ['name', 'age', 'jobs'])

bob = Rec(name='Bob', age=20, jobs=['qa', 'manager'])

print(bob[0])  # Bob
print(bob.name)  # Bob
print(bob.jobs)

O = bob._asdict()
print(O['name'])
print(O['jobs'])
print(O)
