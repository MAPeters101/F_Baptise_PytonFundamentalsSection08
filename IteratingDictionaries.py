d = {
    'key 1': 1,
    'key 2': 2,
    3.14: 'pi'
}

for k in d:
    print(k)

for k in d:
    print(f'd[{k}] = {d[k]}')

for v in d.values():
    print(v)

for t in d.items():
    print(t)

for t in d.items():
    key, value = t
    print(key, value)

for key, value in d.items():
    print(key, value)

for key, value in d.items():
    print(key, value)
    print(f'd[{key}] = {value}')

d = {
    'key 1': 1,
    'key 2': 2,
    3.14: 'pi'
}

d['x'] = 100
print(d)

for k in d:
    print(k)

d['key 1'] = 100

for k in d:
    print(k)

del d['key 1']
print(d)
d['key 1'] = 100
for k in d:
    print(k)