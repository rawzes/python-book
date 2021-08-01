import re
my_string = 'Hello \t Python world!'
match = re.match('Hello [ \t]*(.*)world!', my_string)
print(match.group(1))  # Python
print(match.groups())