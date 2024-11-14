
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}

print('open' in data)
#print(3.14 in data)
print('open' not in data)
print('x' not in data)

l = [1, 2, 3, 4]
print(3 in l)
print(10 not in l)
print()


print(data)
data.clear()
print(data)
print(len(data))
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}
print(len(data))
print()

data_copy = data.copy()
print(data)
print(data_copy)
print(data is data_copy)
data_copy['x'] = 100
print(data)
print(data_copy)
print()

from copy import deepcopy
data_copy = deepcopy(data)
print(data is data_copy)
data_copy['x'] = 100
print(data)
print(data_copy)
print()

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d)
d['b'] = 100
print(d)
print(d_copy)
print()

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d)
print(d)
print(d_copy)

d['a'].append(4)
print(d)
print(d_copy)






