s = 'The knights who say Hi!\n'

print(s.rstrip('\n'))
print(s.upper())
print(s.isalpha())   # false
print(s.endswith('Hi!'))
print(s.startswith('The'))
print(s.find('\n') != -1)