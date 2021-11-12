table = {'1992': "Monthy Python",
         '1994': "Holy Graal",
         '1996': 'Cherry Pick',
         '2000': "Holy Graal"}

year = '1992'

for year in table:
    print(year + '\t' + table[year])

# the same as in example below
for year in table.keys():
    print(year + '\t' + table[year])


# dict comprehension

name = "Holy Graal"
print([key for (key, value) in table.items()])  # ['1992', '1994', '1996']

print([key for (key, value) in table.items() if value == name])  # ['1994']
print([key for key in table.keys() if table[key] == name])  # the same

rec = {'name': 'Bob',
       'positions': ['dev', 'qa'],
       'age': 30,
       'address': {'country': 'US', 'zip': '12345'}}

print(rec['positions'][1])
print(rec['address']['country'])
print(rec['address'])