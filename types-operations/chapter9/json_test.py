import json

name = dict(first_name='roma', last_name='smith')
rec = dict(name=name, job=['qa', 'dev'], salary=490000)

json_object = json.dumps(rec)
print(json_object)

new_obj = json.loads(json_object)
print(new_obj == rec)  # True


# example for dump \ load files into json
json.dump(new_obj, fp=open('test1.json', 'w'), indent=4)
print(open('test1.json').read())
obj2 = json.load(open('test1.json'))
print(obj2)

#  with  - closes file  \ empty buffer automatically
with open(r'd:\test.txt', 'w') as file:
    file.write('some text')

with open(r'd:\test.txt', 'r') as file:
    for line in file:
        print(line)

